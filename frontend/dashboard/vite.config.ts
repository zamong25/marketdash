import path from "node:path";

import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { configDefaults, defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    // Legacy 8-section IA tests target routing retired by the 4-stage migration.
    // The components they cover stay on disk but are out of the typed/tested build.
    exclude: [
      ...configDefaults.exclude,
      // Playwright specs are not vitest suites — keep `npx vitest run` green.
      "e2e/**",
      "src/sections/DashboardWorkspace.test.tsx",
      "src/components/insights/WalletHistoryTable.test.tsx"
    ]
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes("node_modules")) {
            return undefined;
          }
          if (id.includes("lucide-react")) {
            return "vendor-icons";
          }
          if (id.includes("react") || id.includes("react-dom")) {
            return "vendor-react";
          }
          if (id.includes("radix-ui") || id.includes("class-variance-authority")) {
            return "vendor-ui";
          }
          return "vendor";
        }
      }
    }
  },
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  },
  server: {
    port: 5173,
    strictPort: false,
    proxy: (() => {
      const target = "http://127.0.0.1:8000";
      const common = { target, timeout: 120000, proxyTimeout: 120000, changeOrigin: false };
      return {
        "/account": common,
        "/copy-radar": common,
        "/copy-trade-api": common,
        "/dashboard": common,
        "/markets": common,
        "/operations": common,
        "/ops": common,
        "/portfolio": common,
        "/quick-trade": common,
        "/research-board": common,
        "/research": common,
        "/risk": common,
        "/runtime": common,
        "/strategies": common,
        "/wallet-intel": common
      };
    })()
  }
});
