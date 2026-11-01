# ADR 0008: Test Quality Gates

- Status: Accepted
- Date: 2026-04-19
- Phase: Foundation Phase 9

## Context

The repository already had broad unit coverage, but the critical runtime paths
still lacked a few structural guardrails:

- twin execution did not have a focused round-trip integration test
- the execution engines did not have a shared end-to-end smoke around signal
  handling
- validator behavior was covered, but not with a clear integration gate for
  contaminated records being routed away from canonical logs
- schema drift could still slip through if a record shape changed without a
  golden fixture failing
- local quality gates were scattered across individual commands instead of one
  obvious local CI entry point

Phase 9 added those gates without forcing a hosted CI dependency. Phase 10
activates the local hook and adds hosted CI as a thin wrapper around the same
script.

## Decision

- Add integration tests for the twin runner, execution-engine round-trips, and
  validator routing.
- Add schema regression tests for trade-log shape and `pm_events` schema
  alignment.
- Add a local CI wrapper script as the default pre-merge gate.
- Wire `ruff`, `mypy`, `pytest`, and validator sampling through
  `.pre-commit-config.yaml`.
- Keep coverage reporting informational only, with no hard enforcement target
  yet.
- Install the pre-commit hook and run `scripts/ci_local.sh` from hosted CI.

## Consequences

- Critical-path regressions become visible earlier and with less manual log
  inspection.
- A change that alters trade-log field names or types should fail the golden
  schema test instead of quietly drifting into downstream consumers.
- Validator failures remain explicit through the `*_unverified.jsonl` routing
  path.
- Local development and push/PR checks use one repeatable quality gate instead
  of a handful of ad hoc commands.
- Coverage remains a signal, not a policy wall, which keeps the first rollout
  lightweight.

## Alternatives Considered

- Hosted CI only:
  useful later, but too easy to make the local workflow ambiguous.
- Hard coverage threshold now:
  rejected because the phase is about measurement and regression visibility,
  not forcing a specific percentage.
- Hard-blocking quarantine hooks:
  rejected for now so the validator can surface issues without disrupting the
  operator loop.

## Validation

- `PYTHONPATH=. python3 -m pytest tests/ -q --tb=line`
- `PYTHONPATH=. python3 -m pytest tests/test_integration/ -v`
- `PYTHONPATH=. python3 -m pytest tests/test_schema/ -v`
- `bash scripts/ci_local.sh`

## Links

- `docs/tasks/helm_project_foundation/phase_9_tests_ci.md`
- `docs/CONTRIBUTING.md`
- `scripts/ci_local.sh`
- `scripts/validate_trade_logs.py`
- `tests/test_integration/`
- `tests/test_schema/`
