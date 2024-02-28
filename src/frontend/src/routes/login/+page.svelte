<script>
	import { enhance, applyAction } from '$app/forms';
	import { goto } from '$app/navigation';
	import { invalidateAll } from '$app/navigation';
	export let isLoggedIn;
	let error;
</script>

<svelte:head>
	<title>Login</title>
	<meta name="description" content="Login page" />
</svelte:head>

<div class="container">
	<div class="form-container">
		<div class="form-wrapper">
			<form
				method="POST"
				use:enhance={({ formElement, formData, action, cancel }) => {
					return async ({ result }) => {
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
	</div>
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
	.form-wrapper {
		width: 300px;
	}
</style>
