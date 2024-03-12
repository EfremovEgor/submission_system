import { redirect } from '@sveltejs/kit';
import { backend_url } from '../../../../utils';
let conferenceId;
export const actions = {
	default: async ({ fetch, cookies, request, params }) => {
		const values = await request.formData();
		let payload = {};
		payload.title = values.get('title');
		payload.title_ru = values.get('title_ru');
		payload.abstract = values.get('abstract');
		payload.abstract_ru = values.get('abstract_ru');
		payload.keywords = values.get('keywords');
		payload.keywords_ru = values.get('keywords_ru');
		payload.topic_id = parseInt(values.get('topic'));

		payload.conference_id = conferenceId;
		payload.presentation_format = values.get('presentation_format');
		payload.is_ru = !(
			payload.title_ru == null &&
			payload.abstract_ru == null &&
			payload.keywords_ru == null
		);
		let authors = [];
		for (const pair of values.entries()) {
			if (pair[0].startsWith('#')) {
				let isPresent = false;
				let targetPosition;
				for (let i = 0; i < authors.length; i++) {
					const element = authors[i];
					if (element.id == parseInt(pair[0][1])) {
						isPresent = true;
						targetPosition = i;
						break;
					}
				}

				if (!isPresent) {
					targetPosition = authors.length;
					authors.push({ id: parseInt(pair[0][1]) });
				}
				let value = pair[1];
				if (value === 'true') value = true;
				else if (value === 'false') value = false;
				else if (value == null || value.trim().length == 0) value = null;
				authors[targetPosition][pair[0].substring(4)] = value;
			}
		}
		authors.forEach((element) => {
			if (!('is_presenter' in element)) element.is_presenter = false;
			delete element.id;
		});
		payload.authors = authors;
		const res = await fetch(backend_url + '/submissions/', {
			method: 'POST',
			headers: {
				Authorization: 'Bearer ' + cookies.get('token'),
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(payload)
		});
		console.log(res);
		console.log(payload);
	}
};
export const load = async ({ fetch, cookies, request, params }) => {
	if (cookies.get('token') == null) redirect(302, '/login');

	const res = await fetch(backend_url + '/conferences/by_acronym/' + params.conferenceAcronym, {
		method: 'GET'
	});
	const data = await res.json();
	conferenceId = data.id;
	const resUser = await fetch(backend_url + '/users/' + cookies.get('user_id'), {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});

	const dataUser = await resUser.json();
	return { userDetails: dataUser, conference: data };
};
