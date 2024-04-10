import { json } from '@sveltejs/kit';
import { backend_url } from '../../../../utils';
export async function POST({ fetch, cookies, request }) {
	const { id, review_result } = await request.json();

	const payload = JSON.stringify({ review_result: review_result });

	const res = await fetch(backend_url + '/submissions/' + id + '/update_status', {
		method: 'PATCH',
		headers: {
			Authorization: 'Bearer ' + cookies.get('token'),
			'Content-Type': 'application/json'
		},
		body: payload
	});
	const data = await res.json();
	return json({ reqStatus: res.status });
}
