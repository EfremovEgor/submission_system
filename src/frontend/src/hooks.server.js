import { backend_url } from './utils';

export async function handleFetch({ request, fetch }) {
	request = new Request(`http://api:8000${request.url.split(backend_url)[1]}`, request);
	return fetch(request);
}
