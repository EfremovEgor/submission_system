<script>
	import api from '../../axios.js';
	let errorMsg;
	let emailSent = false;
	async function handleOnSubmit(event) {
		const formData = new FormData(event.target);
		const payload = {};
		event.preventDefault();
		formData.forEach((value, key) => (payload[key] = value));
		try {
			const response = await api.post('/auth/register', payload);
			emailSent = true;
		} catch (error) {
			if (error.request.status == 409) {
				errorMsg = 'User with this email already exists';
				return;
			}
			if (error.request.status == 422) {
				errorMsg = 'Email address is invalid';
				return;
			}
		}
	}
</script>

<svelte:head>
	<title>Registration</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	{#if emailSent}
		<div class="success_email-container">
			<p>Email sent</p>
		</div>
	{:else}
		<div class="form-container">
			<div class="form-wrapper">
				<form on:submit={handleOnSubmit}>
					<fieldset>
						<label>
							Email
							<input type="email" name="email" placeholder="Email" autocomplete="email" required />
						</label>
						<label>
							Password
							<input name="password" placeholder="Password" type="password" required />
						</label>
					</fieldset>
					<input type="submit" value="Register" />
				</form>
				<div class="errors">
					{#if errorMsg}
						<p>{errorMsg}</p>
					{/if}
				</div>
				<div class="options-container">
					<p>Already have an account? <a href="/login">Login</a></p>
				</div>
			</div>
		</div>
	{/if}
</div>

<style>
	.errors {
		color: rgba(var(--color-error-50) / 1);
	}
	.form-container,
	.options-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.form-wrapper {
		width: 300px;
	}
</style>
