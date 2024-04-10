import { backend_url } from '../../../utils';
import { redirect } from '@sveltejs/kit';
import { error } from '@sveltejs/kit';
let submissionAuthorId;
export const actions = {
	default: async ({ fetch, cookies, request, params }) => {
		if (cookies.get('user_id') != submissionAuthorId) {
			error(403, { message: 'You are not allowed to delete this submission' });
		}
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
	submissionAuthorId = data.user_id;

	if (res.status == 403) {
		error(403, { message: 'You are not allowed to see this submission' });
	}
	return { submission: data };
};
