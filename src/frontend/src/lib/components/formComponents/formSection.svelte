<script>
	import RequiredStar from './requiredStar.svelte';
	export let sectionHeading;
	export let sectionText;
	export let required = false;
</script>

<div>
	<h4 class="form-section-heading">
		{sectionHeading}
		{#if required}
			<RequiredStar />
		{/if}
	</h4>
	<p class="form-section-text">
		{sectionText}
	</p>
	<article>
		<slot name="inputs" />
	</article>
</div>

<style>
	h4 {
		font-weight: normal;
	}
	.form-section-text {
		margin-left: 20px;
	}
	.form-section-heading {
		display: flex;
		flex-direction: row;
	}
</style>
