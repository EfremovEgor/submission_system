import { redirect } from '@sveltejs/kit';
import verify_token from '../../utils';
import { backend_url } from '../../utils';
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
