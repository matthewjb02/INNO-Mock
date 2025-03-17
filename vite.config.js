import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import { TanStackRouterVite } from "@tanstack/router-plugin/vite";


export default defineConfig({
  base: "/ABM/",
  plugins: [TanStackRouterVite({ autoCodeSplitting: true }), react()],
});