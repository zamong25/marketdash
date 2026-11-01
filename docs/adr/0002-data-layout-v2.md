# ADR 0002: Data Layout V2

- Status: accepted
- Date: 2026-04-19

## Context

The repository accumulated several unrelated data roots:

- `data / realtime`
- `data / pm_events*`
- `data / oracle`
- `data / btc_1s`
- `data / markets`
- `data / historical / trades`
- `data / venue`
- `data / calibration / realistic`
- `data / sampling`, `data / _outcome_cache`, `data / _tmp`

That made it unclear which paths were raw input, normalized history,
regenerable output, or live runtime state.

## Decision

Adopt this canonical layout:

```text
data/
  raw/
  processed/
  derived/
  live/
  quarantine/
```

Path mapping:

- `data / pm_events` -> `data/raw/pm_events`
- `data / pm_events_eth|sol|doge|xrp` -> `data/raw/pm_events/{eth,sol,doge,xrp}`
- `data / btc_1s` -> `data/raw/btc_1s`
- `data / oracle` -> `data/raw/oracle`
- `data / markets` -> `data/raw/markets`
- `data / venue` -> `data/raw/legacy`
- `data / historical / trades` -> `data/processed/trades`
- `data / realtime` -> `data/live/realtime`
- `data / calibration / realistic` -> `data/live/calibration/realistic`
- `data / sampling` -> `data/derived/sampling`
- `data / _outcome_cache` -> `data/derived/outcome_cache`
- `data / _tmp` -> `data/derived/tmp`

## Migration procedure

1. Update code, tests, and config defaults to the v2 paths.
2. Run `PYTHONPATH=. .venv/bin/python scripts/migrate_data_layout_v2.py --dry-run`.
3. Run `PYTHONPATH=. .venv/bin/python scripts/migrate_data_layout_v2.py`.
4. Run the dry-run command again; it should print `No migration actions needed.`
5. Run the test suite.
6. Restart launchd collectors when the operator is ready for new runtime output to land under the v2 layout.

The migration helper is idempotent. If a destination directory already
exists, it merges source contents into it instead of replacing docs or
placeholders.

## Rollback

Rollback is the exact reverse mapping of the paths above, followed by
restoring the old config defaults. Restart launchd collectors only after
the old paths are back in place.

## Launchd compatibility

Existing launchd jobs keep writing wherever their already-running process
has constants and config pointed. Migration alone does not retarget a live
process. After deploying the path changes:

1. leave currently running collectors alone during the filesystem move;
2. verify the new directories exist;
3. restart the launchd jobs when ready so fresh output lands under:
   - `data/live/realtime/`
   - `data/raw/pm_events/`
   - `data/raw/markets/`
   - `data/raw/oracle/`
