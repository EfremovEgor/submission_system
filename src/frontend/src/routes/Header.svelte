<script>
	import { page } from '$app/stores';
	export let isLoggedIn;
</script>

<header>
	<div class="container">
		<nav>
			<ul>
				<li>
					<div class="logo-container">
						<a href="/">
							<h3>ConfChair</h3>
							<h5>Event management system</h5>
						</a>
					</div>
				</li>
				<li aria-current={$page.url.pathname === '/conferences' ? 'page' : undefined}>
					<a href="/conferences">Conferences</a>
				</li>
				{#if isLoggedIn}
					<li aria-current={$page.url.pathname === '/profile' ? 'page' : undefined}>
						<a href="/profile">Profile</a>
					</li>
				{:else}
					<li aria-current={$page.url.pathname === '/login' ? 'page' : undefined}>
						<a href="/login">Login</a>
					</li>
				{/if}
			</ul>
			{#if isLoggedIn}
				<ul>
					<li aria-current={$page.url.pathname === '/logout' ? 'page' : undefined}>
						<a href="/logout">Logout</a>
					</li>
				</ul>
			{/if}
		</nav>
	</div>
</header>

<style>
	.logo-container {
		display: flex;
		flex-direction: column;
		margin-right: 20px;
	}
	.logo-container > a > * {
		margin: 0;
		white-space: nowrap;
	}
	.logo-container > a {
		text-decoration: none;
	}
	header {
		border-radius: var(--pico-border-radius);
		background: var(--pico-card-background-color);
		box-shadow: var(--pico-card-box-shadow);
		margin-bottom: 40px;
	}
</style>
