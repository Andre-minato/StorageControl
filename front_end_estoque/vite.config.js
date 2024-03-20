import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()], 
  server: { 
    watch: null,
    host: '0.0.0.0' 
  }
})
