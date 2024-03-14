<script>
	export let maxLength;
	export let form;
	export let name;
	export let placeholder;
	export let wordCount = 0;
	function handleChange(event) {
		wordCount = event.target.value.split(/\r\n|\r|\n/).length;
	}
</script>

<div class="text_area-wrapper">
	<textarea on:keypress={handleChange} {name} {placeholder} {form} cols="30" rows="10" required />
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
	.text_area-wrapper {
		width: 100%;
	}
</style>
