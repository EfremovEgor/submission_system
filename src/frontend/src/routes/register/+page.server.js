import { redirect } from '@sveltejs/kit';
export const load = async ({ fetch, cookies, request }) => {
	if (cookies.get('token') != null) redirect(302, '/conferences');
};
export const actions = {
	default: async ({ fetch, cookies, request }) => {
		const values = await request.formData();
	}
};
