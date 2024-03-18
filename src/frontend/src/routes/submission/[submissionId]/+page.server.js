import { backend_url } from '../../../utils';
import { redirect } from '@sveltejs/kit';
export const actions = {
	default: async ({ fetch, cookies, request, params }) => {
		const res = await fetch(backend_url + '/submissions/' + params.submissionId, {
			method: 'DELETE',
			headers: {
				Authorization: 'Bearer ' + cookies.get('token')
			}
		});
		redirect(302, '/profile');
	}
};

export const load = async ({ fetch, cookies, request, params }) => {
	const res = await fetch(backend_url + '/submissions/' + params.submissionId, {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});
	const data = await res.json();

	return { submission: data };
};
