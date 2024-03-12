import { backend_url } from '../../../../utils';
export const load = async ({ fetch, cookies, request, params }) => {
	const res = await fetch(backend_url + '/submissions/from_conference/' + params.conferenceId, {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});
	const data = await res.json();

	return { submissions: data };
};
