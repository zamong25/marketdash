import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import { App } from "./App";
import { installChunkReloadRecovery } from "./chunkReloadRecovery";
import "./styles.css";

installChunkReloadRecovery();

createRoot(document.getElementById("root") as HTMLElement).render(
  <StrictMode>
    <App />
  </StrictMode>
);
