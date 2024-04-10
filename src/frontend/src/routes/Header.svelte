<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/logo.png';
	export let isLoggedIn;
	export let user;
</script>

<header>
	<div class="container">
		<nav>
			<ul>
				<li>
					<div class="logo-container">
						<a href="/">
							<img class="logo" src={logo} alt="ConfChair Logo" />
						</a>
					</div>
				</li>
				<li aria-current={$page.url.pathname === '/conferences' ? 'page' : undefined}>
					<a href="/conferences">Call For Papers</a>
				</li>
				{#if isLoggedIn}
					<li aria-current={$page.url.pathname === '/profile' ? 'page' : undefined}>
						<a href="/profile">Author</a>
					</li>
					{#if user.reviewer_in.length > 0}
						<li aria-current={$page.url.pathname === '/reviewer' ? 'page' : undefined}>
							<a href="/reviewer">Reviewer</a>
						</li>
					{/if}
					{#if user.chair_in.length > 0}
						<li aria-current={$page.url.pathname === '/chair' ? 'page' : undefined}>
							<a href="/chair">Chair</a>
						</li>
					{/if}
				{/if}
			</ul>
			{#if isLoggedIn}
				<ul>
					<li aria-current={$page.url.pathname === '/logout' ? 'page' : undefined}>
						<a href="/logout">Logout</a>
					</li>
				</ul>
			{:else}
				<ul>
					<li aria-current={$page.url.pathname === '/login' ? 'page' : undefined}>
						<a href="/login">Sign in</a>
					</li>
					<li aria-current={$page.url.pathname === '/register' ? 'page' : undefined}>
						<a href="/register">Create account</a>
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
	.logo {
		max-height: 70px;
	}
</style>
