<script>
	import { page } from '$app/stores';
	export let isLoggedIn;
</script>

<header>
	<div class="container">
		<nav>
			<ul>
				<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
					<a href="/">Home</a>
				</li>
				<li aria-current={$page.url.pathname === '/conferences' ? 'page' : undefined}>
					<a href="/conferences">Conferences</a>
				</li>
				{#if isLoggedIn}
					<li aria-current={$page.url.pathname === '/profile' ? 'page' : undefined}>
						<a href="/profile">Profile</a>
					</li>
					<li aria-current={$page.url.pathname === '/logout' ? 'page' : undefined}>
						<a href="/logout">Logout</a>
					</li>
				{:else}
					<li aria-current={$page.url.pathname === '/login' ? 'page' : undefined}>
						<a href="/login">Login</a>
					</li>
					<li aria-current={$page.url.pathname === '/register' ? 'page' : undefined}>
						<a href="/register">Register</a>
					</li>
				{/if}
			</ul>
		</nav>
	</div>
</header>

<style>
</style>
