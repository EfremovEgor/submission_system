import verify_token from '../utils';
import { backend_url } from '../utils';
export const load = async ({ fetch, cookies, request }) => {
	const token = cookies.get('token');
	const isValid = await verify_token(token, fetch);
	if (!isValid) {
		cookies.delete('token', { path: '/' });
		cookies.delete('token_type', { path: '/' });
		cookies.delete('user_id', { path: '/' });
		cookies.delete('username', { path: '/' });
		return;
	}
	const res = await fetch(backend_url + '/users/' + cookies.get('user_id'), {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});
	const data = await res.json();
	if (cookies.get('token') != null) {
		return { user: data, user_id: parseInt(cookies.get('user_id')) };
	}
	return { user: data, user_id: null };
};
