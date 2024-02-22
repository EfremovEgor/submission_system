import { redirect } from '@sveltejs/kit';
import verify_token from '../../utils';
export const actions = {
	default: async ({ fetch, cookies, request }) => {
		cookies.delete('token', { path: '/' });
		cookies.delete('token_type', { path: '/' });
		cookies.delete('user_id', { path: '/' });
		cookies.delete('username', { path: '/' });
		redirect(302, '/conferences');
	}
};
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') == null) redirect(302, '/conferences');
};
