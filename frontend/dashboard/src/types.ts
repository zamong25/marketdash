export type DashboardNavItem = {
  anchor: string;
  label: string;
  active: boolean;
};

export type DashboardSectionId =
  | "system-map"
  | "discover"
  | "strategy"
  | "trade"
  | "monitor";

export type DashboardSection = {
  id: DashboardSectionId;
  label: string;
  kicker: string;
  description: string;
};

export const DASHBOARD_SECTIONS: DashboardSection[] = [
  {
    description: "돈과 판단이 어느 구간에 있는지, 기계·규칙·기록까지 한눈에 봅니다.",
    id: "system-map",
    kicker: "운영",
    label: "시스템 지도"
  },
  {
    description: "누가 벌고 어느 시장에 edge가 있나 — 거래할 만한 후보를 read-only로 찾습니다.",
    id: "discover",
    kicker: "탐색",
    label: "🔍 탐색"
  },
  // Strategy top-level hidden with its subviews; see the restore block in navigation.ts.
  // {
  //   description: "이게 진짜 버는 패턴인가 — 패턴·백테스트·승격 게이트를 판정합니다.",
  //   id: "strategy",
  //   kicker: "전략",
  //   label: "🧪 전략"
  // },
  {
    description: "검색한 이벤트의 관련 시장을 열고 CLOB 호가, 주문 티켓, 라이브 게이트로 실주문합니다.",
    id: "trade",
    kicker: "거래",
    label: "💰 거래"
  },
  {
    description: "봇이 지금 실제로 버는가 + 주문을 내도 안전한가를 한눈에 봅니다.",
    id: "monitor",
    kicker: "성과",
    label: "📊 성과"
  }
];

export function isDashboardSectionId(value: string): value is DashboardSectionId {
  return DASHBOARD_SECTIONS.some((section) => section.id === value);
}

export function dashboardSectionFromHash(hash: string): DashboardSectionId | null {
  const value = hash.trim().replace(/^#/, "").split("?", 1)[0].toLowerCase();
  return isDashboardSectionId(value) ? value : null;
}

export function dashboardWalletFromHash(hash: string): string | null {
  const wallet = dashboardHashParams(hash).get("wallet")?.trim() ?? "";
  return wallet || null;
}

// The wallet a workspace should adopt when it (re)binds to `section`, read from
// the hash so a cross-workspace deep-link (e.g. 장부 → #discover?...&wallet=0x…)
// carries its subject even though that jump fires a single hashchange the old
// section's listener ignores. Returns null when the hash targets another section
// or omits the wallet, so a plain section switch never clobbers the current one.
export function dashboardDeepLinkWallet(
  hash: string,
  section: DashboardSectionId
): string | null {
  if (dashboardSectionFromHash(hash) !== section) {
    return null;
  }
  return dashboardWalletFromHash(hash);
}

export function dashboardViewFromHash(hash: string): string | null {
  const view = dashboardHashParams(hash).get("view")?.trim() ?? "";
  return view || null;
}

export function dashboardSearchQueryFromHash(hash: string): string | null {
  const query = dashboardHashParams(hash).get("q")?.trim() ?? "";
  return query || null;
}

export function dashboardTradeMarketFromHash(hash: string): string | null {
  const market = dashboardHashParams(hash).get("market")?.trim() ?? "";
  return market || null;
}

export function dashboardSectionHash(
  section: DashboardSectionId,
  options: {
    marketId?: string | null;
    searchQuery?: string | null;
    viewId?: string | null;
    walletAddress?: string | null;
  } = {}
): string {
  const params = new URLSearchParams();
  const walletAddress = options.walletAddress?.trim();
  if (section === "discover" && walletAddress) {
    params.set("wallet", walletAddress);
  }
  const searchQuery = options.searchQuery?.trim();
  if (section === "trade" && searchQuery) {
    params.set("q", searchQuery);
  }
  const marketId = options.marketId?.trim();
  if (section === "trade" && marketId) {
    params.set("market", marketId);
  }
  const viewId = options.viewId?.trim();
  if (viewId) {
    params.set("view", viewId);
  }
  const query = params.toString();
  if (!query) {
    return `#${section}`;
  }
  return `#${section}?${params.toString()}`;
}

function dashboardHashParams(hash: string): URLSearchParams {
  const query = hash.trim().replace(/^#/, "").split("?")[1] ?? "";
  return new URLSearchParams(query);
}

export type DashboardKpi = {
  element_id: string;
  label: string;
  tone: "" | "alert" | "scout" | string;
};

export type DashboardFetchJob = {
  label: string;
  url: string;
  renderer: string;
};

export type DashboardManifest = {
  version: number;
  nav: DashboardNavItem[];
  kpis: DashboardKpi[];
  fetch_plan: {
    core: DashboardFetchJob[];
    priority: DashboardFetchJob[];
    detail: DashboardFetchJob[];
    detail_batch_size: number;
  };
};

export type PanelStage = "core" | "priority" | "detail";

export type PanelFetchState = DashboardFetchJob & {
  durationMs: number | null;
  error: string | null;
  loadedAt: string | null;
  ok: boolean;
  stage: PanelStage;
  status: "pending" | "loading" | "ok" | "error";
};

export type KpiValueMap = Record<string, string | number>;
