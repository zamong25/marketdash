import {
  Activity,
  BookOpen,
  BookOpenText,
  ClipboardList,
  CopyPlus,
  Crosshair,
  FlaskConical,
  Gauge,
  HandCoins,
  Map as MapIcon,
  MapPinned,
  Network,
  Radar,
  type LucideIcon
} from "lucide-react";

import type { DashboardSectionId } from "./types";

// ---------------------------------------------------------------------------
// New information architecture: 대분류 (section) > 소분류 (subview = one screen).
//
//   🔍 탐색   (discover) : 수익지갑 · 카피 명단 · 기회 큐 · 지갑 분석 · 연못 지도
//   💰 거래   (trade)    : (소분류 없음 — QuickTradeDashboard 단일 화면)
//   📊 성과   (monitor)  : 관제 · 장부
//
// Each 소분류 id maps 1:1 to a screen component in DashboardWorkspace. The id is
// what lands in the url hash (`#discover?view=wallets`) so screens are
// deep-linkable and survive reloads.
// ---------------------------------------------------------------------------

export type DiscoverWorkspaceViewId =
  | "live-leaderboard"
  | "copy-roster"
  | "cluster-console"
  | "guru-dossier"
  | "copy-radar"
  | "wallet-analytics"
  | "copy-console"
  | "markets"
  | "pond-map";
export type StrategyWorkspaceViewId = "patterns" | "backtest" | "promotion";
export type MonitorWorkspaceViewId = "bot" | "mission-control" | "shadow-ledger" | "account";

export type WorkspaceViewId =
  | DiscoverWorkspaceViewId
  | StrategyWorkspaceViewId
  | MonitorWorkspaceViewId;

export type WorkspaceSubview<T extends string = WorkspaceViewId> = {
  description: string;
  /** Live UI feature flag. Hidden screens stay implemented but leave navigation. */
  hidden?: boolean;
  id: T;
  label: string;
  /** Optional lucide icon shown beside the 소분류 label in the sidebar. */
  icon?: LucideIcon;
};

/** Mission control is retired by default; an explicit build flag restores it. */
export function missionControlEnabled(value: string | boolean | undefined): boolean {
  return value === true || value === "true";
}

const WORKSPACE_VIEW_STORAGE_PREFIX = "venue-dashboard.workspace-view.";
const SELECTED_WALLET_STORAGE_KEY = "venue-dashboard.selected-wallet";

export const SECTION_ICONS: Record<DashboardSectionId, LucideIcon> = {
  "system-map": MapPinned,
  discover: Radar,
  strategy: FlaskConical,
  trade: HandCoins,
  monitor: Activity
};

// --- 🔍 탐색 ---------------------------------------------------------------
export const DISCOVER_WORKSPACE_VIEWS: Array<
  WorkspaceSubview<DiscoverWorkspaceViewId>
> = [
  {
    description:
      "실시간 수집 → 지갑 → 활발 → 손익 → 수익. 집계 깔때기가 살아 움직이고, 손익순 리더보드(닉네임·전적·시장)까지 한 화면에서.",
    id: "live-leaderboard",
    label: "수익 지갑"
  },
  {
    description:
      "지금 실제로 카피 중인 지갑 명단 — 뽑힌 근거(그들의 3주 성적)와 우리 기본 전략 장부 성적, 활동/판단 보류/정지 상태까지.",
    icon: ClipboardList,
    id: "copy-roster",
    label: "카피 명단"
  },
  {
    description:
      "같은 주인으로 의심되는 지갑 묶음(봇팜) — 0초 동시진입 증거·리드 지갑·개별 성적·우리 카피 성적을 군집 단위로 봅니다.",
    icon: Network,
    id: "cluster-console",
    label: "군집 관제"
  },
  {
    description:
      "고수 한 명씩 깊게 분석한 판정 기록 — 유형 지도·도씨에 원문·유형/지갑 규칙 카드·주간 역스캔 발굴 후보를 한 화면에서.",
    icon: BookOpenText,
    id: "guru-dossier",
    label: "고수 도씨에"
  },
  {
    description:
      "수익 지갑이 방금 담은 거래를 감지 순서대로 — 지금 따라갈 만한지 판정과 함께 봅니다.",
    icon: Crosshair,
    id: "copy-radar",
    label: "기회 큐"
  },
  {
    description:
      "한 지갑의 손익곡선·카테고리·시간대·확률 보정에 더해 따라하기 점수·백테스트·패턴 그룹까지 한 화면에서 봅니다.",
    id: "wallet-analytics",
    label: "지갑 분석"
  },
  {
    description:
      "카피하려는 지갑을 등록하고, 새 거래가 뜰 때 현재 시장 조건으로 따라갈지 보류할지 판정합니다.",
    // hidden 2026-07-11 by operator approval (WP-76)
    // why: 카피 실행 is unused in the operator's current frontend workflow
    // how to restore: remove `hidden` (screen/component stays implemented)
    hidden: true,
    icon: CopyPlus,
    id: "copy-console",
    label: "카피 실행"
  },
  {
    description: "어떤 시장이 활발하고 들여다볼 만한지 찾습니다.",
    // hidden 2026-07-11 by operator approval (WP-76)
    // why: 시장 발굴 is unused in the operator's current frontend workflow
    // how to restore: remove `hidden` (screen/component stays implemented)
    hidden: true,
    id: "markets",
    label: "시장 발굴"
  },
  {
    description:
      "다음 주에 어느 판에서 낚시할지 — 시장 카테고리별 판 크기·이기는 지갑 비율·패자 출혈을 기회 점수 순으로 봅니다.",
    icon: MapIcon,
    id: "pond-map",
    label: "연못 지도"
  }
];

// --- 🧪 전략 ---------------------------------------------------------------
export const STRATEGY_WORKSPACE_VIEWS: Array<
  WorkspaceSubview<StrategyWorkspaceViewId>
> = [
  // hidden 2026-07-08 by operator approval (docs/tasks/frontend_pruning_v0/)
  // why: copy_engine.db frozen 2026-06-09; function superseded by copy-radar cohort gates + replay harness + constitution gate
  // how to restore: uncomment these entries (screens/components were intentionally left in place)
  // {
  //   description: "비슷한 스타일의 지갑들을 묶어 반복되는 패턴을 봅니다.",
  //   id: "patterns",
  //   label: "패턴 분석"
  // },
  // {
  //   description: "이 패턴을 과거에 적용하면 실제로 벌었는지 검증합니다.",
  //   id: "backtest",
  //   label: "백테스트"
  // },
  // {
  //   description: "실전 후보로 올릴 자격이 되는지 게이트로 판정합니다.",
  //   id: "promotion",
  //   label: "승격"
  // }
];

// --- 📊 성과 ---------------------------------------------------------------
export const MONITOR_WORKSPACE_VIEWS: Array<
  WorkspaceSubview<MonitorWorkspaceViewId>
> = [
  {
    description:
      "감지 서비스·리그·심판·실탄 안전 조건·다음 루틴을 한 화면에서 봅니다.",
    // hidden by default after the 2026-07-12 phase-2 migration (WP-129)
    // escape hatch: build with VITE_ENABLE_MISSION_CONTROL=true
    hidden: !missionControlEnabled(import.meta.env.VITE_ENABLE_MISSION_CONTROL),
    icon: Gauge,
    id: "mission-control",
    label: "관제"
  },
  {
    description: "봇이 지금 실제로 얼마나 버는지 — 손익·전략 성적.",
    // hidden 2026-07-11 by operator approval (WP-76)
    // why: 봇 성과 is unused in the operator's current frontend workflow
    // how to restore: remove `hidden` (screen/component stays implemented)
    hidden: true,
    id: "bot",
    label: "봇 성과"
  },
  {
    description:
      "수익 지갑을 가상으로 따라 산 결과 — 누적·오늘 손익, 정산 성적, 진행 중 포지션을 실 데이터로.",
    icon: BookOpen,
    id: "shadow-ledger",
    label: "장부"
  },
  {
    description: "잔고·노출 한도·비상 정지 — 주문 내도 안전한지.",
    // hidden 2026-07-11 by operator approval (WP-76)
    // why: 계정·안전 is unused in the operator's current frontend workflow
    // how to restore: remove `hidden` (screen/component stays implemented)
    hidden: true,
    id: "account",
    label: "계정·안전"
  }
];

// Single source of truth for implemented screens, including feature-flagged
// entries. Trade has no 소분류 — it is the standalone QuickTradeDashboard.
const ALL_SECTION_SUBVIEWS: Record<
  DashboardSectionId,
  Array<WorkspaceSubview>
> = {
  "system-map": [],
  discover: DISCOVER_WORKSPACE_VIEWS,
  strategy: STRATEGY_WORKSPACE_VIEWS,
  trade: [],
  monitor: MONITOR_WORKSPACE_VIEWS
};

// Public navigation contains visible screens only. Hidden screens remain in the
// implemented arrays and render switches above/below, ready to restore by flag.
export const SECTION_SUBVIEWS: Record<
  DashboardSectionId,
  Array<WorkspaceSubview>
> = Object.fromEntries(
  Object.entries(ALL_SECTION_SUBVIEWS).map(([section, views]) => [
    section,
    views.filter((view) => !view.hidden)
  ])
) as Record<DashboardSectionId, Array<WorkspaceSubview>>;

/** The 소분류 shown first when a 대분류 is opened without a `view` hint. */
export function defaultWorkspaceView(
  sectionId: DashboardSectionId
): WorkspaceViewId | null {
  return SECTION_SUBVIEWS[sectionId][0]?.id ?? null;
}

/** Resolve a raw hash `view` value to a valid 소분류 id for the section. */
export function resolveWorkspaceView(
  sectionId: DashboardSectionId,
  value: string | null
): WorkspaceViewId | null {
  const views = SECTION_SUBVIEWS[sectionId];
  if (views.length === 0) {
    return null;
  }
  const match = value && views.find((view) => view.id === value);
  if (match) {
    return match.id;
  }
  const hiddenMatch =
    value &&
    ALL_SECTION_SUBVIEWS[sectionId].some(
      (view) => view.id === value && view.hidden
    );
  if (hiddenMatch) {
    return views[0].id;
  }
  const stored = readStoredWorkspaceView(sectionId);
  if (stored && views.some((view) => view.id === stored)) {
    return stored;
  }
  return views[0].id;
}

export function isWorkspaceSubviewId<T extends string>(
  views: Array<WorkspaceSubview<T>>,
  value: string
): value is T {
  return views.some((view) => view.id === value);
}

export function readStoredWorkspaceView(
  sectionId: DashboardSectionId
): WorkspaceViewId | null {
  const value = readStorageValue(workspaceViewStorageKey(sectionId));
  if (!value) {
    return null;
  }
  return isWorkspaceSubviewId(SECTION_SUBVIEWS[sectionId], value)
    ? (value as WorkspaceViewId)
    : null;
}

export function writeStoredWorkspaceView(
  sectionId: DashboardSectionId,
  viewId: string
): void {
  try {
    safeLocalStorage()?.setItem(workspaceViewStorageKey(sectionId), viewId);
  } catch {
    // Storage can be unavailable in privacy-restricted browser contexts.
  }
}

export function readStoredWalletAddress(): string | null {
  const value = readStorageValue(SELECTED_WALLET_STORAGE_KEY)?.trim() ?? "";
  return value || null;
}

export function writeStoredWalletAddress(address: string | null): void {
  const storage = safeLocalStorage();
  if (!storage) {
    return;
  }
  try {
    const value = address?.trim() ?? "";
    if (value) {
      storage.setItem(SELECTED_WALLET_STORAGE_KEY, value);
    } else {
      storage.removeItem(SELECTED_WALLET_STORAGE_KEY);
    }
  } catch {
    // Storage can be unavailable in privacy-restricted browser contexts.
  }
}

function workspaceViewStorageKey(sectionId: DashboardSectionId): string {
  return `${WORKSPACE_VIEW_STORAGE_PREFIX}${sectionId}`;
}

function readStorageValue(key: string): string | null {
  try {
    return safeLocalStorage()?.getItem(key) ?? null;
  } catch {
    return null;
  }
}

function safeLocalStorage(): Storage | null {
  if (typeof window === "undefined") {
    return null;
  }
  try {
    return window.localStorage;
  } catch {
    return null;
  }
}
