<script>
	export let maxLength;
	export let form;
	export let name;
	export let data = '';
	export let placeholder;
	export let wordCount = 0;
	wordCount = data?.trim().split(/\r\n|\r|\n/).length;

	function handleChange(event) {
		wordCount = event.target.value.trim().split(/\r\n|\r|\n/).length;
	}
</script>

<div class="text_area-wrapper">
	<textarea on:keypress={handleChange} {name} {placeholder} {form} cols="30" rows="10" required
		>{data}</textarea
	>
	<p class="word_counter">{wordCount}</p>
</div>

<style>
	textarea {
		padding-right: 20px !important;
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
	.text_area-wrapper {
		width: 100%;
		margin-bottom: -80px;
	}
</style>
