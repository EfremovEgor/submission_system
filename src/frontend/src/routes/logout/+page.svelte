<script>
</script>

<svelte:head>
	<title>Logout</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	<article class="form-container">
		<h3>Do you want to sign out?</h3>
		<form class="logout-form" method="POST">
			<input class="logout" type="submit" name="choice" value="Yes" />
			<a class="stay" style="width:100%" role="button" href="/conferences">No</a>
		</form>
	</article>
</div>

<style>
	.stay {
		background-color: rgb(71, 164, 23);
		border-color: rgb(71, 164, 23);
		transition: all 0.3s;
	}
	.stay:hover {
		background-color: rgb(64, 150, 20);
		border-color: rgb(64, 150, 20);
		transition: all 0.3s;
	}
	.logout {
		background-color: rgb(238, 64, 46);
		border-color: rgb(238, 64, 46);
		transition: all 0.3s;
	}
	.logout:hover {
		background-color: rgb(134, 29, 19);
		border-color: rgb(134, 29, 19);
		transition: all 0.3s;
	}
	.logout-form {
		display: flex;
		width: 80%;
		justify-content: space-around;
	}
	.logout-form > * {
		height: 60px;
		max-width: 30%;
	}
	.form-container {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		min-height: 400px;
		width: fit-content;
		margin: auto;
		min-width: 400px;
		padding: 40px 20px;
	}
</style>
