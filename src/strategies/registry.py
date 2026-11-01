"""Strategy registry — single source of truth for discovering, resolving, and
instantiating strategies by name.

Public surface:
  - ``@register_strategy(name, capabilities=..., aliases=..., emoji=...)``
    — decorator placed on a strategy class. The decorator records the class
    under ``name`` in the registry, with optional alias lookups (e.g.
    ``p1_confident_direction_tight`` → resolves to ``p1_confident_direction``).
  - ``resolve(name) -> StrategyInfo`` — return the canonical info for ``name``,
    matching either canonical names or aliases. Raises ``KeyError`` if unknown.
  - ``list_canonical() -> list[StrategyInfo]`` — every registered canonical
    strategy, ordered by registration time (insertion order).
  - ``aliases_of(canonical) -> tuple[str, ...]`` — aliases for one canonical
    strategy, or empty tuple if ``canonical`` is unknown.
  - ``capability_descriptor_for(name) -> StrategyCapabilityDescriptor`` —
    convenience helper for replay / parity validators.

Discovery model: importing ``src.strategies`` triggers eager import of every
``src/strategies/<name>.py`` module that contains an ``@register_strategy``
decorator (see ``src/strategies/__init__.py``). New strategies become
discoverable by the loader simply by dropping a decorated class file into the
package — no edits to loader, config_version, capability registry, or the
runner emoji map are required.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, FrozenSet, TypeVar

from src.core.capabilities import StrategyCapabilityDescriptor


T = TypeVar("T")


@dataclass(frozen=True)
class StrategyInfo:
    """Registry entry for a single canonical strategy."""

    name: str
    cls: type
    capabilities: StrategyCapabilityDescriptor
    aliases: tuple[str, ...] = ()
    emoji: str = ""

    @property
    def class_path(self) -> str:
        """``module.QualName`` for compatibility with legacy STRATEGY_REGISTRY consumers."""
        return f"{self.cls.__module__}.{self.cls.__name__}"


# Insertion-ordered registry of canonical strategies.
_REGISTRY: dict[str, StrategyInfo] = {}
# Fast alias → canonical lookup.
_ALIAS_MAP: dict[str, str] = {}


def _ensure_capabilities(
    name: str,
    capabilities: StrategyCapabilityDescriptor | dict | FrozenSet[str] | None,
) -> StrategyCapabilityDescriptor:
    """Coerce the decorator's ``capabilities`` argument into a descriptor."""
    if capabilities is None:
        return StrategyCapabilityDescriptor(strategy_name=name)
    if isinstance(capabilities, StrategyCapabilityDescriptor):
        # Replace ``strategy_name`` with the registered name to enforce coherence.
        if capabilities.strategy_name != name:
            return StrategyCapabilityDescriptor(
                strategy_name=name,
                required_snapshot_fields=capabilities.required_snapshot_fields,
                minimum_snapshot_level=capabilities.minimum_snapshot_level,
                execution_profile=capabilities.execution_profile,
                notes=capabilities.notes,
            )
        return capabilities
    if isinstance(capabilities, dict):
        return StrategyCapabilityDescriptor(
            strategy_name=name,
            required_snapshot_fields=tuple(
                capabilities.get("required_snapshot_fields", ())
            ),
            minimum_snapshot_level=capabilities.get(
                "minimum_snapshot_level", "snapshot"
            ),
            execution_profile=capabilities.get("execution_profile", "single_leg_taker"),
            notes=tuple(capabilities.get("notes", ())),
        )
    if isinstance(capabilities, (frozenset, set, tuple, list)):
        # Treat as a bag of required-field tags (legacy convenience).
        return StrategyCapabilityDescriptor(
            strategy_name=name,
            required_snapshot_fields=tuple(sorted(capabilities)),
        )
    raise TypeError(f"Unsupported capabilities type: {type(capabilities)!r}")


def register_strategy(
    *,
    name: str,
    capabilities: StrategyCapabilityDescriptor | dict | FrozenSet[str] | None = None,
    aliases: tuple[str, ...] | list[str] = (),
    emoji: str = "",
) -> Callable[[type], type]:
    """Decorator: record a strategy class under ``name`` (and aliases).

    Re-registering the same canonical name with the same class is a no-op
    (idempotent) so reload-style imports don't error. Re-registering with a
    different class raises ``ValueError`` to surface a real conflict.
    """
    aliases_tuple = tuple(aliases)

    def _decorator(cls: type) -> type:
        descriptor = _ensure_capabilities(name, capabilities)
        info = StrategyInfo(
            name=name,
            cls=cls,
            capabilities=descriptor,
            aliases=aliases_tuple,
            emoji=emoji,
        )

        if name in _REGISTRY:
            existing = _REGISTRY[name]
            same_class = existing.cls is cls or (
                # Module reload produces a new class object with same qualified
                # name from the same module; treat as idempotent re-registration.
                existing.cls.__module__ == cls.__module__
                and existing.cls.__qualname__ == cls.__qualname__
            )
            if same_class:
                _REGISTRY[name] = info
            else:
                raise ValueError(
                    f"Duplicate strategy registration: name={name!r} already bound to "
                    f"{existing.class_path}, cannot bind to {info.class_path}"
                )
        else:
            _REGISTRY[name] = info

        # Alias map: every alias points to the canonical name.
        for alias in aliases_tuple:
            if alias == name:
                continue
            existing_canonical = _ALIAS_MAP.get(alias)
            if existing_canonical and existing_canonical != name:
                raise ValueError(
                    f"Alias {alias!r} already routes to {existing_canonical!r}; "
                    f"cannot route to {name!r}"
                )
            _ALIAS_MAP[alias] = name

        return cls

    return _decorator


def resolve(name: str) -> StrategyInfo:
    """Return the StrategyInfo for ``name``, accepting canonical or alias forms.

    Raises ``KeyError`` if the name is unknown. Triggers ``_bootstrap_strategies``
    on first call if registry is empty (for callers that import the module
    before ``src.strategies.__init__`` has run discovery).
    """
    if not _REGISTRY:
        _bootstrap_strategies()
    canonical = _ALIAS_MAP.get(name, name)
    if canonical not in _REGISTRY:
        raise KeyError(f"Unknown strategy: {name!r}")
    return _REGISTRY[canonical]


def list_canonical() -> list[StrategyInfo]:
    """Return all canonical strategies in registration order."""
    if not _REGISTRY:
        _bootstrap_strategies()
    return list(_REGISTRY.values())


def aliases_of(canonical: str) -> tuple[str, ...]:
    """Return aliases registered for one canonical strategy (or empty tuple)."""
    if not _REGISTRY:
        _bootstrap_strategies()
    info = _REGISTRY.get(canonical)
    return info.aliases if info else ()


def capability_descriptor_for(name: str) -> StrategyCapabilityDescriptor:
    """Return capabilities for ``name`` (canonical or alias).

    Falls back to a minimal descriptor for unknown names so callers (replay
    validators, parity scorers) keep working when probing names that aren't
    yet registered (e.g. fixture-only test names).
    """
    try:
        return resolve(name).capabilities
    except KeyError:
        return StrategyCapabilityDescriptor(strategy_name=name)


def _bootstrap_strategies() -> None:
    """Eagerly import every strategy module so their decorators run.

    Skips modules whose import fails (e.g. archived legacy strategies whose
    .py files were already moved out of ``src/strategies/``). The runner does
    not need failed modules; only registered ones are reachable via ``resolve``.
    """
    import importlib
    import pkgutil

    import src.strategies as pkg

    for finder, modname, ispkg in pkgutil.iter_modules(pkg.__path__):
        # Skip subpackages (helpers/, models/) and the registry itself.
        if ispkg or modname in {"registry", "capability_registry"}:
            continue
        try:
            importlib.import_module(f"src.strategies.{modname}")
        except Exception:
            # Don't let a single broken legacy module poison discovery.
            continue


def _reset_for_tests() -> None:
    """Test-only helper to clear registry state."""
    _REGISTRY.clear()
    _ALIAS_MAP.clear()
