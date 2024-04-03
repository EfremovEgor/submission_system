import { redirect } from '@sveltejs/kit';
import { backend_url } from '../../utils';
export const actions = {
	default: async ({ fetch, cookies, request }) => {
		const values = await request.formData();
		let urlencoded = new URLSearchParams();
		urlencoded.append('username', values.get('email'));
		urlencoded.append('password', values.get('password'));
		urlencoded.append('grant_type', '');
		urlencoded.append('scope', '');
		urlencoded.append('client_id', '');
		urlencoded.append('client_secret', '');

		const res = await fetch(backend_url + '/auth/token', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded'
			},
			body: urlencoded
		});
		if (res.status == 404) {
			return { status: 404 };
		}
		if (res.status == 401) {
			return { status: 401 };
		}
		if (res.status == 403) {
			return { status: 403 };
		}
		const data = await res.json();
		cookies.set('token', data.access_token, {
			path: '/',
			secure: true
		});
		cookies.set('token_type', data.token_type, {
			path: '/',
			secure: true
		});
		cookies.set('user_id', data.user_id, {
			path: '/',
			secure: true
		});
		cookies.set('username', data.username, {
			path: '/',
			secure: true
		});

		redirect(302, '/profile');
	}
};
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') != null) redirect(302, '/profile');
};
