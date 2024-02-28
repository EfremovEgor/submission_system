<script>
	import { enhance, applyAction } from '$app/forms';
	let error;
	let sentEmail = false;
	let isBusy = false;
</script>

<svelte:head>
	<title>Registration</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	{#if sentEmail}
		<article class="verification_sent-container">
			<h3>Verification email has been sent</h3>
			<p>If you haven't recieved email, please check spam folder</p>
		</article>
	{:else}
		<article aria-busy={isBusy} class="form-container">
			{#if !isBusy}
				<h3>Registration</h3>
				<div class="form-wrapper">
					<form
						method="POST"
						use:enhance={({ formElement, formData, action, cancel }) => {
							isBusy = true;
							return async ({ result }) => {
								if (result.data.status == 200) {
									sentEmail = true;
									return;
								}
								if (result.data.status == 422) {
									error = 'Invalid email';
									return;
								}
								if (result.data.status == 409) {
									error = 'User with this email already exists';

									return;
								}
							};
						}}
					>
						<fieldset>
							<label>
								Email
								<input
									type="email"
									name="email"
									placeholder="Email"
									autocomplete="email"
									required
								/>
							</label>
							<label>
								Password
								<input name="password" placeholder="Password" type="password" required />
							</label>
						</fieldset>
						{#if error}
							<div class="errors">
								<p>{error}</p>
							</div>
						{/if}
						<input type="submit" value="Register" />
					</form>
					<div class="options-container">
						<p>Already have an account? <a href="/login">Login</a></p>
					</div>
				</div>
			{/if}
		</article>
	{/if}
</div>

<style>
	.errors > p {
		color: rgb(238, 64, 46);
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.form-container,
	.options-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.form-container {
		min-height: 400px;
		width: fit-content;
		margin: auto;
		min-width: 400px;
		padding: 40px 0;
	}
	.options-container > p {
		margin: 0px;
	}
	.form-wrapper {
		width: 300px;
	}
	.verification_sent-container {
		margin: auto;
		width: fit-content;
		min-height: 300px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.verification_sent-container > h3 {
		color: rgb(71, 164, 23);
	}
</style>
