import { backend_url } from '../../../utils';
export const load = async ({ fetch, cookies, request, params }) => {
	const res = await fetch(backend_url + '/conferences/' + params.conferenceId, {
		method: 'GET'
	});
	const data = await res.json();
	let isReviewer = false;
	data.reviewers.forEach((element) => {
		if (cookies.get('user_id') == element.id) isReviewer = true;
	});

	return { conference: data, isReviewer: isReviewer };
};
