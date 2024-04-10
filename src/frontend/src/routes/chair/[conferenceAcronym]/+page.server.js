import { redirect } from '@sveltejs/kit';
import { backend_url } from '../../../utils';
export const load = async ({ fetch, cookies, request, params }) => {
	if (cookies.get('token') == null) redirect(302, '/login');
	const res = await fetch(backend_url + '/users/' + cookies.get('user_id'), {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});
	if (res.status == 401) {
		cookies.delete('token', { path: '/' });
		cookies.delete('token_type', { path: '/' });
		cookies.delete('user_id', { path: '/' });
		cookies.delete('username', { path: '/' });
		redirect(302, '/login');
	}
	const conferenceRes = await fetch(
		backend_url + '/conferences/by_acronym/' + params.conferenceAcronym,
		{
			method: 'GET'
		}
	);
	const conference = await conferenceRes.json();
	const data = await res.json();
	return { profile: data, conference: conference };
};
