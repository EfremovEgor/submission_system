<script>
	export let data;
	let isValid = data.isValid;
</script>

<div class="container">
	{#if isValid}
		<h3>Email confirmed</h3>
		<p>Please proceed to <a href="/login">login page</a></p>
	{:else}
		<h3>Verification link is invalid</h3>
	{/if}
</div>
