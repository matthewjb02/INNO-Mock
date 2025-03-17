import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import {
    RouterProvider,
    createRouter,
    createHashHistory,
} from "@tanstack/react-router";
import { routeTree } from "./view/pages/root";

const hashHistory = createHashHistory();

// Ensure the router is correctly created without TypeScript type enforcement
const router = createRouter({
    history: hashHistory,
    routeTree,
});

// Render the application
const rootElement = document.getElementById("root");

if (rootElement) {
    createRoot(rootElement).render(
        <StrictMode>
            <RouterProvider router={router} />
        </StrictMode>
    );
} else {
    console.error("Root element not found");
}