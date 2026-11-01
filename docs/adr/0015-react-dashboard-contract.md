# ADR 0015: React Dashboard Contract

Date: 2026-05-10

## Status

Accepted

## Context

The original `/dashboard` route served a single large FastAPI HTML string with
embedded CSS, JavaScript, navigation, KPI card definitions, and endpoint fetch
plans. That was useful for proving API contracts, but it was not a maintainable
foundation for the requested professional dashboard.

The long-running goal requires a modular React dashboard that can grow into
wallet intelligence, market scanning, strategy evidence, simulation, risk, and
research-log views without turning into another monolith.

The user has also made the dashboard design requirement explicit: the final
surface should be professional, visually clear, easy to scan, and implemented
with Tailwind CSS plus shadcn/ui rather than accumulating unstructured custom
CSS.

On 2026-05-12 the user clarified that the dashboard should use
`https://usstockdash-b8x5cmaj.manus.space` as a design-feel reference. The
project must not copy that site's content or product domain, but should bring
over the Korean-first product feel: calm professional color, good icon usage,
clear type hierarchy, purposeful page layout, disciplined information density,
and tables/cards/panels that make complex screens understandable to a new
operator.

The user later clarified that "easy to scan at a glance" does not mean placing
every table and chart on one long page. The dashboard must behave like a
professional operations console: persistent sidebar categories, focused
workspace pages, and subviews per category so operators can move between
account, markets, wallets, strategies, operations, and research without visual
overload.

## Decision

Use `src/api/dashboard_manifest.py` as the read-only UI contract for dashboard
navigation, KPI cards, and staged fetch plans.

Keep the legacy FastAPI `/dashboard` shell working while building the React
dashboard in `frontend/dashboard/`.

Use Tailwind CSS and shadcn/ui as the default styling and component layer for
the React dashboard. shadcn/ui components should be copied into the project as
owned source and adapted through local design tokens, variants, and feature
components. The migration should be incremental, starting with primitives such
as cards, badges, tables, tabs, tooltips, dialogs, scroll areas, and command or
search surfaces.

Keep the information architecture category-first. The top-level React shell
must expose a sidebar for dashboard categories. Each category owns a focused
workspace section and can expose subviews through local navigation. New
features should land in the relevant workspace rather than expanding the
overview or creating another all-in-one page. The overview is a triage surface,
not the full product.

Current workspace categories are now Korean product surfaces:

- 오늘의 시장 브리핑: daily triage, cross-system status, next safe actions
- 시장 발견: full-market discovery, scanner, pins, orderbook, quality,
  replay evidence
- 거래 워크벤치: locked/read-only manual search, market detail, ticket preview
  foundation; no live order route by default
- 전략 연구소: strategy insights, evidence, drilldowns, leads, scorecards,
  simulation evidence
- 지갑 인사이트: profitable-wallet discovery, source review, cohorts, replay
  gates, repeatability, details, copyability patterns
- 리스크 & 계정: capital, allowances, balances, holdings, portfolio/PnL,
  exposure limits, live-readiness gates
- 리서치 기록: decisions, memory/search, actions, backlog
- 시스템 상태: operations queue, run history, execution quality, logs,
  manifest health

The React dashboard consumes:

- `/dashboard/manifest`
- `/risk/status`
- `/runtime/status`
- `/strategies`
- `/wallet-intel/*`

The frontend is organized as:

- `src/hooks/` for staged data loading
- `src/selectors.ts` for converting raw API payloads into typed view models
- `src/components/` for reusable dashboard UI
- `src/App.tsx` for top-level layout composition
- `src/navigation.ts` for sidebar categories and workspace subviews
- `src/sections/` for category-level workspace pages
- `src/components/ui/` for owned shadcn/ui primitives

## Consequences

Positive:

- The API remains the source of truth.
- The React frontend can grow module-by-module without breaking the legacy
  dashboard.
- Navigation, KPI cards, and panel fetch plans are no longer duplicated as
  hardcoded UI constants.
- Tailwind/shadcn provides a consistent design-token and component foundation,
  reducing custom CSS drift as the dashboard grows.
- Category workspaces keep dense data usable without turning the dashboard into
  a single unreadable scroll page.
- Sidebar and subview routing make future wallet, strategy, market, and
  research tools easier to add without rewriting the shell.
- Production serving now prefers React on `/dashboard` when a build exists, with
  the legacy FastAPI HTML retained only as a build-missing fallback.

Tradeoffs:

- During migration there are still two dashboard implementations, but FastAPI
  routes operators to React first when `frontend/dashboard/dist/index.html`
  exists.
- Some view-model derivation currently happens client-side in selectors; this
  is acceptable for early UI migration but may move server-side when the
  contract stabilizes.
- Production static serving is not solved by this ADR. It should be addressed
  separately after the React dashboard has real feature coverage.
- Tailwind and shadcn/ui do not replace information architecture, data
  correctness, or visual QA. The dashboard still needs deliberate page
  composition, responsive checks, and screenshots as it evolves.
- A category-first shell creates more route/view state to maintain. Hash routing
  and local storage should remain tested so deep links and last-used subviews
  keep working.

## Verification

Checks used during the initial migration:

```bash
.venv/bin/python -m pytest -q tests/test_api/test_dashboard_ui.py tests/test_api/test_wallet_intel_endpoint.py
cd frontend/dashboard && npm run build
```

Playwright screenshots were used to visually verify the React dashboard at
`http://127.0.0.1:5173/`.
