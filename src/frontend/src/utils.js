export const backend_url = 'http://127.0.0.1:8000';
async function verify_token(token) {
	const res = await fetch(backend_url + '/auth/verify_token', {
		method: 'GET',
		headers: {
			Authorization: 'Bearer ' + token
		}
	});
	if (res.status == 200) return true;
	return false;
}
export default verify_token;
