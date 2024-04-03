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
			<h3>Sign in</h3>
			<div class="form-wrapper">
				<form
					autocomplete="on"
					method="POST"
					use:enhance={({ formElement, formData, action, cancel }) => {
						isBusy = true;
						return async ({ result }) => {
							isBusy = false;
							if (result.type === 'redirect') {
								isLoggedIn = true;
								location.reload();

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
							<input
								id="email"
								type="email"
								name="email"
								placeholder="Email"
								autocomplete="email"
								required
							/>
						</label>
						<label>
							<input
								id="password"
								name="password"
								placeholder="Password"
								type="password"
								required
							/>
						</label>
					</fieldset>
					{#if error}
						<div class="errors">
							<p>{error}</p>
						</div>
					{/if}
					<input class="blue-button" type="submit" value="Login" />
				</form>

				<div class="options-container">
					<p>Don't have an account? <a href="/register">Create account</a></p>
				</div>
			</div>
		{/if}
	</article>
</div>

<style>
	.login-button {
		background-color: transparent;
		color: var(--pico-primary);
	}
	.login-button:hover {
		background-color: var(--pico-primary-hover);
		color: white;
	}
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
