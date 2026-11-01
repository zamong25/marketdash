import type {
  DashboardFetchJob,
  DashboardManifest,
  PanelFetchState,
  PanelStage
} from "./types";

const DEFAULT_TIMEOUT_MS = 15_000;
const LOCAL_API_BASE_URL = "http://127.0.0.1:8000";

function apiUrl(url: string): string {
  if (!url.startsWith("/") || typeof window === "undefined") {
    return url;
  }
  const isLocalDashboard =
    (window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost") &&
    window.location.port === "5173";
  return isLocalDashboard ? `${LOCAL_API_BASE_URL}${url}` : url;
}

export async function fetchJson<T>(
  url: string,
  timeoutMs = DEFAULT_TIMEOUT_MS,
  externalSignal?: AbortSignal
): Promise<T> {
  return requestJson<T>(url, { method: "GET" }, timeoutMs, externalSignal);
}

export async function requestJson<T>(
  url: string,
  init: RequestInit = {},
  timeoutMs = DEFAULT_TIMEOUT_MS,
  externalSignal?: AbortSignal
): Promise<T> {
  const controller = new AbortController();
  const timeout = window.setTimeout(() => controller.abort(), timeoutMs);
  const onExternalAbort = () => controller.abort();
  if (externalSignal) {
    if (externalSignal.aborted) controller.abort();
    else externalSignal.addEventListener("abort", onExternalAbort);
  }
  try {
    const response = await fetch(apiUrl(url), { ...init, signal: controller.signal });
    if (!response.ok) {
      let detail = `${response.status} ${response.statusText}`;
      try {
        const payload = (await response.json()) as { detail?: unknown };
        if (typeof payload.detail === "string") {
          detail = payload.detail;
        } else if (
          payload.detail &&
          typeof payload.detail === "object" &&
          "reason" in payload.detail
        ) {
          detail = String((payload.detail as { reason?: unknown }).reason ?? detail);
        }
      } catch {
        // Keep the HTTP status message.
      }
      const error = new Error(detail) as Error & { status?: number };
      error.status = response.status;
      throw error;
    }
    return (await response.json()) as T;
  } finally {
    window.clearTimeout(timeout);
    if (externalSignal) externalSignal.removeEventListener("abort", onExternalAbort);
  }
}

export async function postJson<T>(
  url: string,
  body: unknown,
  timeoutMs = DEFAULT_TIMEOUT_MS
): Promise<T> {
  return requestJson<T>(
    url,
    {
      body: JSON.stringify(body),
      headers: { "Content-Type": "application/json" },
      method: "POST"
    },
    timeoutMs
  );
}

export async function deleteJson<T>(
  url: string,
  body: unknown,
  timeoutMs = DEFAULT_TIMEOUT_MS
): Promise<T> {
  return requestJson<T>(
    url,
    {
      body: JSON.stringify(body),
      headers: { "Content-Type": "application/json" },
      method: "DELETE"
    },
    timeoutMs
  );
}

export function fetchManifest(): Promise<DashboardManifest> {
  return fetchJson<DashboardManifest>("/dashboard/manifest");
}

export type MarketSearchToken = {
  outcome: string;
  price: number | null;
  token_id: string;
};

export type MarketSearchRules = {
  blockers: string[];
  checks: Array<{
    detail: string;
    label: string;
    missing_code: string;
    status: string;
  }>;
  review_items: string[];
  review_status: string;
};

export type MarketSearchMarket = {
  accepting_orders: boolean;
  active: boolean;
  archived: boolean;
  best_ask: number | null;
  best_bid: number | null;
  category: string;
  closed: boolean;
  clob_token_ids: string[];
  condition_id: string;
  description: string;
  enable_orderbook: boolean;
  end_date: string;
  event_slug: string;
  event_title: string;
  game_start_time: string;
  last_trade_price: number | null;
  liquidity: number | null;
  market_id: string;
  matched_fields: string[];
  order_min_size: number | null;
  order_tick_size: number | null;
  outcome_prices: Array<number | null>;
  outcomes: string[];
  question: string;
  question_id: string;
  rank_score: number;
  restricted: boolean;
  resolution_source: string;
  rules?: MarketSearchRules;
  slug: string;
  spread: number | null;
  status_label: string;
  tags: string[];
  tokens: MarketSearchToken[];
  tradeable: boolean;
  url: string;
  volume: number | null;
  volume_24h: number | null;
};

export type MarketSearchResponse = {
  generated_at: string;
  markets: MarketSearchMarket[];
  query: string;
  safety: {
    live_trading_allowed: boolean;
    places_orders: boolean;
    queries_exchange_balances: boolean;
    read_only: boolean;
    source: string;
    uses_order_api: boolean;
    uses_private_keys: boolean;
  };
  source?: {
    audit_error?: string;
    audit_log_path?: string;
    audit_logged?: boolean;
    audit_optional?: boolean;
    detail_enriched_count?: number;
    detail_error_count?: number;
    detail_lookup_count?: number;
  };
  status: string;
  summary: {
    closed_count: number;
    event_count: number;
    has_more: boolean;
    market_count: number;
    tokenized_count: number;
    total_results: number;
    tradeable_count: number;
  };
};

export function fetchMarketSearch(query: string, limit = 12): Promise<MarketSearchResponse> {
  const params = new URLSearchParams({
    limit: String(limit),
    q: query
  });
  return fetchJson<MarketSearchResponse>(`/markets/search?${params.toString()}`);
}

export type OrderbookLevel = {
  price: number;
  size: number;
};

export type OrderbookPreviewBook = {
  ask_depth_3: number;
  asks: OrderbookLevel[];
  best_ask: number | null;
  best_ask_size: number | null;
  best_bid: number | null;
  best_bid_size: number | null;
  bid_depth_3: number;
  bids: OrderbookLevel[];
  hash: string;
  last_trade_price: number | null;
  market: string;
  min_order_size: number | null;
  multi_outcome: boolean;
  spread: number | null;
  tick_size: number | null;
  timestamp: string;
  token_id: string;
};

export type TradePreview = {
  average_price: number | null;
  best_price: number | null;
  blockers: string[];
  depth_levels_used: number;
  estimated_notional: number;
  fillable_shares: number;
  limit_price: number | null;
  remaining_shares: number;
  selected_token_id: string;
  shares_requested: number;
  side: "BUY" | "SELL" | string;
  worst_price: number | null;
};

export type OrderbookRiskGate = {
  blockers: string[];
  checks: Array<{
    name: string;
    status: string;
    value: unknown;
  }>;
  recommended_action: string;
  status: "blocked" | "review" | "pass" | string;
  warnings: string[];
};

export type OrderbookPreviewResponse = {
  books: OrderbookPreviewBook[];
  generated_at: string;
  notes: string[];
  preview: TradePreview;
  risk_gate: OrderbookRiskGate;
  request: {
    limit_price: number | null;
    market_tradeable: boolean | null;
    existing_position_exposure_usd: number;
    existing_position_shares: number;
    selected_token_id: string;
    shares: number;
    side: string;
    token_ids: string[];
  };
  safety: MarketSearchResponse["safety"];
  source: {
    docs: string[];
    endpoint: string;
  };
  status: string;
  summary: {
    best_ask: number | null;
    best_bid: number | null;
    blocker_count: number;
    book_count: number;
    estimated_notional: number;
    fillable_shares: number;
    risk_status: string;
    selected_has_book: boolean;
    spread: number | null;
  };
};

export function fetchOrderbookPreview({
  existingPositionExposureUsd,
  existingPositionShares,
  limitPrice,
  marketTradeable,
  selectedTokenId,
  shares,
  side,
  tokenIds
}: {
  existingPositionExposureUsd: number;
  existingPositionShares: number;
  limitPrice: number | null;
  marketTradeable: boolean | null;
  selectedTokenId: string;
  shares: number;
  side: "BUY" | "SELL";
  tokenIds: string[];
}): Promise<OrderbookPreviewResponse> {
  const params = new URLSearchParams({
    selected_token_id: selectedTokenId,
    existing_position_exposure_usd: String(existingPositionExposureUsd),
    existing_position_shares: String(existingPositionShares),
    shares: String(shares),
    side,
    token_ids: tokenIds.join(",")
  });
  if (marketTradeable !== null) {
    params.set("market_tradeable", String(marketTradeable));
  }
  if (limitPrice !== null) {
    params.set("limit_price", String(limitPrice));
  }
  return fetchJson<OrderbookPreviewResponse>(`/markets/orderbook-preview?${params.toString()}`);
}

export type ManualTradeIntentPayload = {
  market: Partial<MarketSearchMarket>;
  order: {
    limit_price: number | null;
    shares: number;
    side: "BUY" | "SELL";
  };
  orderbook_preview: {
    preview: TradePreview;
    request: OrderbookPreviewResponse["request"];
    risk_gate: OrderbookPreviewResponse["risk_gate"];
    summary: OrderbookPreviewResponse["summary"];
  };
  portfolio_context: {
    estimated_notional: number;
    existing_position_exposure_usd: number;
    existing_position_shares: number;
    position_count: number;
  };
  selected_token: MarketSearchToken;
  source: "dashboard_trade_workbench";
};

export type ManualTradeIntentResponse = {
  generated_at: string;
  intent: unknown;
  safety: {
    intent_only: boolean;
    live_trading_allowed: boolean;
    places_orders: boolean;
    queries_exchange_balances: boolean;
    requires_separate_live_enablement: boolean;
    uses_order_api: boolean;
    uses_private_keys: boolean;
  };
  source: { log_path: string };
  status: "saved" | string;
  summary: {
    blocker_count: number;
    estimated_notional: number | null;
    intent_id: string;
    live_order_allowed: boolean;
    market_slug: string;
    outcome: string;
    projected_position_exposure_usd: number;
    question: string;
    risk_status: string;
    shares: number;
    side: string;
  };
};

export function saveManualTradeIntent(
  payload: ManualTradeIntentPayload
): Promise<ManualTradeIntentResponse> {
  return postJson<ManualTradeIntentResponse>("/operations/manual-trade-intents", payload);
}

export type MarketPinPayload = {
  market: Partial<MarketSearchMarket>;
  query: string;
  source: "dashboard_trade_workbench" | "market_discovery_search";
};

export type MarketPinSaveResponse = {
  generated_at: string;
  pin: unknown;
  safety: {
    live_trading_allowed: boolean;
    places_orders: boolean;
    queries_exchange_balances: boolean;
    research_only: boolean;
    uses_order_api: boolean;
    uses_private_keys: boolean;
  };
  source: {
    pins_path: string;
    upserted_existing: boolean;
  };
  status: "saved" | string;
  summary: {
    label: string;
    live_order_allowed: boolean;
    pin_count: number;
    pin_state: string;
    window_slug: string;
  };
};

export function saveMarketPin(payload: MarketPinPayload): Promise<MarketPinSaveResponse> {
  return postJson<MarketPinSaveResponse>("/markets/pins", payload);
}

export function makePanelState(job: DashboardFetchJob, stage: PanelStage): PanelFetchState {
  return {
    ...job,
    durationMs: null,
    error: null,
    loadedAt: null,
    ok: false,
    stage,
    status: "pending"
  };
}
