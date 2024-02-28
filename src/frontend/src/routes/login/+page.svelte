<script>
	import { enhance } from '$app/forms';

	export let isLoggedIn;
	let isBusy = false;
	let error;
</script>

<svelte:head>
	<title>Login</title>
	<meta name="description" content="Login page" />
</svelte:head>

<div class="container">
	<article aria-busy={isBusy} class="form-container">
		{#if !isBusy}
			<h3>Login</h3>
			<div class="form-wrapper">
				<form
					method="POST"
					use:enhance={({ formElement, formData, action, cancel }) => {
						isBusy = true;
						return async ({ result }) => {
							isBusy = false;
							console.log(result);
							if (result.type === 'redirect') {
								isLoggedIn = true;
								// location.reload();

								return;
							}
							if (result.data.status == 401) {
								error = 'Wrong credentials';
								return;
							}
							if (result.data.status == 404) {
								error = 'No user with this email found';

								return;
							}
							if (result.data.status == 403) {
								error = "Email hasn't been verified yet";

								return;
							}
						};
					}}
				>
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
					{#if error}
						<div class="errors">
							<p>{error}</p>
						</div>
					{/if}
					<input type="submit" value="Login" />
				</form>

				<div class="options-container">
					<p>Don't have an account? <a href="/register">Register</a></p>
				</div>
			</div>
		{/if}
	</article>
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
</style>
