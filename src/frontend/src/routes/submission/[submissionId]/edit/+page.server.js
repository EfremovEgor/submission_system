import { backend_url } from '../../../../utils';
import { error } from '@sveltejs/kit';
import { redirect } from '@sveltejs/kit';
let submissionId;
let submissionAuthorId;
export const actions = {
	default: async ({ fetch, cookies, request, params }) => {
		const values = await request.formData();
		let payload = {};
		if (cookies.get('user_id') != submissionAuthorId) {
			error(403, { message: 'You are not allowed to edit this submission' });
		}
		payload.title = values.get('title');
		payload.title_ru = values.get('title_ru');
		payload.abstract = values.get('abstract');
		payload.abstract_ru = values.get('abstract_ru');
		payload.keywords = values.get('keywords');
		payload.keywords_ru = values.get('keywords_ru');
		payload.topic_id = parseInt(values.get('topic'));
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
			if (element.id == parseInt(values.get('is_presenter'))) element.is_presenter = true;
			if (!('is_presenter' in element)) element.is_presenter = false;
			if (!('is_corresponding' in element)) element.is_corresponding = false;
			delete element.id;
		});
		payload.authors = authors;

		const res = await fetch(backend_url + '/submissions/' + submissionId, {
			method: 'PATCH',
			headers: {
				Authorization: 'Bearer ' + cookies.get('token'),
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(payload)
		});
		return { status: res.status };
	}
};

export const load = async ({ parent, fetch, cookies, request, params }) => {
	const submission_res = await fetch(backend_url + '/submissions/' + params.submissionId, {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token')
		}
	});

	const submission_data = await submission_res.json();
	submissionId = submission_data.id;
	submissionAuthorId = submission_data.user_id;
	const conference_res = await fetch(
		backend_url + '/conferences/' + submission_data.conference_id,
		{
			method: 'GET',
			headers: {
				Authorization: 'Bearer ' + cookies.get('token')
			}
		}
	);
	const conference_data = await conference_res.json();
	const { user } = await parent();
	let accessGranted = false;

	if (user.id == submission_data.user_id) accessGranted = true;
	if (!accessGranted) {
		error(403, { message: 'You are not allowed to edit this submission' });
	}
	return { submission: submission_data, conference: conference_data };
};
