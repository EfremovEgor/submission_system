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
			return;
		}
		if (res.status == 401) {
			return;
		}

		const data = await res.json();
		cookies.set('token', data.access_token, {
			path: '/',
			httpOnly: false,
			sameSite: 'strict'
		});
		cookies.set('token_type', data.token_type, {
			path: '/',
			httpOnly: false,
			sameSite: 'strict'
		});
		cookies.set('user_id', data.user_id, {
			path: '/',
			httpOnly: false,
			sameSite: 'strict'
		});
		cookies.set('username', data.username, {
			path: '/',
			httpOnly: false,
			sameSite: 'strict'
		});
		redirect(302, '/conferences');
	}
};
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') != null) redirect(302, '/conferences');
};
