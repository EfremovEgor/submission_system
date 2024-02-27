import verify_token from '../utils';

export const load = async ({ fetch, cookies, request }) => {
	const token = cookies.get('token');
	if (!(await verify_token(token, fetch))) {
		cookies.delete('token', { path: '/' });
		cookies.delete('token_type', { path: '/' });
		cookies.delete('user_id', { path: '/' });
		cookies.delete('username', { path: '/' });
		return;
	}
	if (cookies.get('token') != null) return { user_id: parseInt(cookies.get('user_id')) };
	return { user_id: null };
};
