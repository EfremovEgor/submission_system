export const backend_url = '/backend';
async function verify_token(token, fetch) {
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
export function convertToDate(datetime) {
	const dateObj = new Date(datetime);
	return dateObj.toLocaleDateString();
}

export const titles = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.'];
