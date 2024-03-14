<script>
	export let name;
	export let placeholder;
	export let wordCount = 0;
	function handleChange(event) {
		wordCount = event.target.value.trim().split(/\s+/).length;
	}
</script>

<div class="input-wrapper">
	<input type="text" on:keypress={handleChange} {placeholder} {name} required />
	<p class="word_counter">{wordCount}</p>
</div>

<style>
	.word_counter {
		position: relative;
		text-align: right;
		top: -60px;
		left: 96%;
		width: fit-content;
		font-size: small;
	}
	.input-wrapper {
		width: 100%;
	}
</style>
