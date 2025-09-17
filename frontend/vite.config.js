import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,        // default port
    host: "localhost", // change to "0.0.0.0" if you want to access from another device
  },
});
