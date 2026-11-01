import { useEffect, useState } from "react";
import { ShieldCheck } from "lucide-react";

import { Sidebar } from "./components/Sidebar";
import { useDashboardData } from "./hooks/useDashboardData";
import { DashboardHeader } from "./sections/DashboardHeader";
import { DashboardWorkspace } from "./sections/DashboardWorkspace";
import {
  DASHBOARD_SECTIONS,
  dashboardSectionFromHash,
  dashboardSectionHash,
  type DashboardSectionId
} from "./types";

const SIDEBAR_COLLAPSED_KEY = "qt-sidebar-collapsed";

// Every 4-stage screen (DiscoverView / StrategyView / QuickTradeDashboard /
// MonitorView) renders its own PageHeader, so the legacy DashboardHeader topbar
// is suppressed for all of them to avoid a doubled header.
const IMMERSIVE_SECTIONS: DashboardSectionId[] = [
  "system-map",
  "discover",
  "strategy",
  "trade",
  "monitor"
];

function isImmersiveSection(section: DashboardSectionId): boolean {
  return IMMERSIVE_SECTIONS.includes(section);
}

function readInitialSidebarCollapsed(): boolean {
  if (typeof window === "undefined") return false;
  try {
    const stored = window.localStorage.getItem(SIDEBAR_COLLAPSED_KEY);
    if (stored !== null) {
      return stored === "1";
    }
  } catch {
    // ignore
  }
  return window.matchMedia("(max-width: 900px)").matches;
}

export function App() {
  const [activeSection, setActiveSection] = useState<DashboardSectionId>(() =>
    dashboardSectionFromHash(window.location.hash) ?? "monitor"
  );
  const [sidebarCollapsed, setSidebarCollapsed] = useState<boolean>(readInitialSidebarCollapsed);

  useEffect(() => {
    try {
      window.localStorage.setItem(SIDEBAR_COLLAPSED_KEY, sidebarCollapsed ? "1" : "0");
    } catch {
      // ignore
    }
  }, [sidebarCollapsed]);
  const {
    errorCount,
    insights,
    loadingCount,
    manifest,
    manifestError,
    okCount,
    panelStates
  } = useDashboardData(activeSection);

  useEffect(() => {
    function handleHashChange() {
      const nextSection = dashboardSectionFromHash(window.location.hash);
      if (nextSection) {
        setActiveSection(nextSection);
      }
    }

    window.addEventListener("hashchange", handleHashChange);
    return () => window.removeEventListener("hashchange", handleHashChange);
  }, []);

  function handleSectionChange(section: DashboardSectionId) {
    setActiveSection(section);
    const nextHash = dashboardSectionHash(section);
    if (window.location.hash !== nextHash) {
      window.history.replaceState(null, "", nextHash);
    }
  }

  // manifest를 한 번이라도 받았으면 이후 일시적 로드 실패(예: 화면 전환 중 요청
  // 취소)에는 전체 fallback으로 가지 않고 기존 manifest를 유지한다. 첫 로드부터
  // 실패한 경우(manifest 없음)에만 에러 페이지를 보여준다.
  if (manifestError && !manifest && activeSection !== "system-map") {
    return (
      <main className="fallback">
        <ShieldCheck aria-hidden="true" />
        <h1>Dashboard manifest unavailable</h1>
        <p>{manifestError}</p>
      </main>
    );
  }

  return (
    <div className={`app-shell ${sidebarCollapsed ? "is-sidebar-collapsed" : ""}`}>
      <Sidebar
        activeSection={activeSection}
        collapsed={sidebarCollapsed}
        onSectionChange={handleSectionChange}
        onToggleCollapsed={() => setSidebarCollapsed((value) => !value)}
        sections={DASHBOARD_SECTIONS}
      />

      <main className={`workspace ${activeSection === "trade" ? "workspace--trade" : ""} ${activeSection === "system-map" ? "workspace--system-map" : ""}`}>
        {isImmersiveSection(activeSection) ? null : (
          <DashboardHeader
            errorCount={errorCount}
            loadingCount={loadingCount}
            okCount={okCount}
            panelTotal={panelStates.length}
          />
        )}

        <DashboardWorkspace
          activeSection={activeSection}
          insights={insights}
          kpis={manifest?.kpis ?? []}
          panelStates={panelStates}
        />
      </main>
    </div>
  );
}
