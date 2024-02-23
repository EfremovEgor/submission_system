import { backend_url } from '../../utils';

export const load = async ({ fetch, cookies, request, params }) => {
	const res = await fetch(backend_url + '/conferences', {
		method: 'GET'
	});
	const data = await res.json();
	return { conferences: data };
};
