import { redirect } from '@sveltejs/kit';
import { backend_url } from '../../utils';
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') != null) redirect(302, '/conferences');
};
export const actions = {
	default: async ({ fetch, cookies, request }) => {
		const values = await request.formData();
		const payload = {};
		values.forEach((value, key) => (payload[key] = value));
		const data = JSON.stringify(payload);
		const res = await fetch(backend_url + '/auth/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: data
		});
	}
};
