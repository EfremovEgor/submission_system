<script>
</script>

<svelte:head>
	<title>Login</title>
	<meta name="description" content="Login page" />
</svelte:head>

<div class="container">
	<div class="form-container">
		<div class="form-wrapper">
			<form method="POST">
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
				<input type="submit" value="Login" />
			</form>
			<div class="options-container">
				<p>Don't have an account? <a href="/register">Register</a></p>
			</div>
		</div>
	</div>
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
