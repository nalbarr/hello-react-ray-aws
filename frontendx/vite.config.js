import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [react()]
// })

// NAA. MP needs this for CORS
// - https://rubenr.dev/en/cors-vite-vue/
export default defineConfig({
  server: {
    proxy: {   
      "/simples": {
        target: "http://localhost:8000/simples",
        changeOrigin: true,
        secure: false,
      },
    },    
  },
  plugins: [react()],
})