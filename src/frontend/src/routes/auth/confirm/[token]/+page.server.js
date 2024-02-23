import { backend_url } from '../../../../utils';
export const load = async ({ fetch, cookies, request, params }) => {
	const res = await fetch(backend_url + '/auth/confirm/' + params.token, {
		method: 'GET'
	});
	let isValid = res.status == 200;

	return { isValid: isValid };
};
