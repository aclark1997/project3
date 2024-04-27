import React from "react";
import { createRoot } from "react-dom/client";

async function main() {
  const rootElt = document.getElementById("app");
  const root = createRoot(rootElt);

  root.render(React.createElement("h1", null, "I'm In Hell"));
}

window.onload=main
