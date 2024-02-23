import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
export default defineConfig({
	plugins: [sveltekit()]

	// server: {
	// 	proxy: {
	// 		// '/api': 'http://api:8000'
	// 		'/api': {
	// 			target: 'http://api.host.docker.internal',

	// 			secure: false,
	// 			rewrite: (path) => path.replace(/^\/api/, '')
	// 		}
	// 	}
	// }
});
