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
	input {
		padding-right: 30px !important;
	}
	.word_counter {
		position: relative;
		text-align: right;
		top: -50px;
		height: 40px;
		left: 98%;
		width: fit-content;
		font-size: small;
	}
	.input-wrapper {
		width: 100%;
		margin-bottom: -80px;
	}
</style>
