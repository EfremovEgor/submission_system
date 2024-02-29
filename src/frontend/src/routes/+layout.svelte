<script>
	import Header from './Header.svelte';
	import './styles.css';
	export let data;
	const isLoggedIn = data.user_id != null;
</script>

<div class="app">
	<Header {isLoggedIn} />

	<main>
		<slot />
	</main>
</div>

<style>

</style>
