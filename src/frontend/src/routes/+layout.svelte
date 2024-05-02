<script>
	import Header from './Header.svelte';
	import Footer from './Footer.svelte';
	import '@picocss/pico/';

	import './styles.css';
	export let data;
	const isLoggedIn = data.user_id != null;
</script>

<div class="app">
	<Header {isLoggedIn} user={data.user} />

	<main>
		<slot />
	</main>
	<Footer />
</div>

<style>
	main {
		min-height: 100vh;
	}
</style>
