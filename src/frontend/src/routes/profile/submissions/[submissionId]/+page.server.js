import { backend_url } from '../../../../utils';
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
