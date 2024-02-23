import { redirect } from '@sveltejs/kit';
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

		const res = await fetch('http://127.0.0.1:8000/auth/token', {
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
		cookies.set('token', data.access_token, { path: '/', httpOnly: true, sameSite: 'strict' });
		cookies.set('token_type', data.token_type, { path: '/', httpOnly: true, sameSite: 'strict' });
		cookies.set('user_id', data.user_id, { path: '/', httpOnly: true, sameSite: 'strict' });
		cookies.set('username', data.username, { path: '/', httpOnly: true, sameSite: 'strict' });
		redirect(302, '/conferences');
	}
};
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') != null) redirect(302, '/conferences');
};
