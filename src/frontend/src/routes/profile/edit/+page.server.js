import { redirect } from '@sveltejs/kit';
import { backend_url } from '../../../utils';
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') == null) redirect(302, '/login');
	const res = await fetch(backend_url + '/users/' + cookies.get('user_id'), {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});
	const data = await res.json();
	return { profile: data };
};
export const actions = {
	default: async ({ fetch, cookies, request }) => {
		const values = await request.formData();
		let object = {};
		for (const pair of values.entries()) {
			if (pair[1] != null && pair[1].trim().length != 0) object[pair[0]] = pair[1];
		}
		const data = JSON.stringify(object);
		const res = await fetch(backend_url + '/users/' + cookies.get('user_id') + '/', {
			method: 'PATCH',
			headers: {
				Authorization: 'Bearer ' + cookies.get('token'),
				'Content-Type': 'application/json'
			},
			body: data
		});
		if (res.status == 401) {
			cookies.delete('token', { path: '/' });
			cookies.delete('token_type', { path: '/' });
			cookies.delete('user_id', { path: '/' });
			cookies.delete('username', { path: '/' });
			redirect(302, '/login');
		}
		redirect(302, '/profile');
	}
};
