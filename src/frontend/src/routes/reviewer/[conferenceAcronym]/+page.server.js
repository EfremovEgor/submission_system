import { backend_url } from '../../../utils';
export const load = async ({ fetch, cookies, request, params }) => {
	const conferenceRes = await fetch(
		backend_url + '/conferences/by_acronym/' + params.conferenceAcronym,
		{
			method: 'GET'
		}
	);
	const conference = await conferenceRes.json();
	const res = await fetch(backend_url + '/submissions/from_conference/' + conference.id, {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});
	const data = await res.json();

	return { conference: conference, submissions: data };
};
