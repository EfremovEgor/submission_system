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
	if (res.status == 401) {
		cookies.delete('token', { path: '/' });
		cookies.delete('token_type', { path: '/' });
		cookies.delete('user_id', { path: '/' });
		cookies.delete('username', { path: '/' });
		redirect(302, '/login');
	}

	const data = await res.json();
	return { profile: data };
};
export const actions = {
	default: async ({ fetch, cookies, request }) => {
		const values = await request.formData();
		let data = {
			title: values.get('title'),
			first_name: values.get('first_name'),
			last_name: values.get('last_name'),
			surname: values.get('surname'),
			affilation: values.get('affilation'),
			country: values.get('country'),
			city: values.get('city'),
			state: values.get('state'),
			orcid_id: values.get('orcid_id'),
			web_page: values.get('web_page')
		};

		const payload = JSON.stringify(data);
		const res = await fetch(backend_url + '/users/' + cookies.get('user_id') + '/', {
			method: 'PATCH',
			headers: {
				Authorization: 'Bearer ' + cookies.get('token'),
				'Content-Type': 'application/json'
			},
			body: payload
		});
		console.log(await res.json());
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
