<script>
	import RequiredStar from '../../../formComponents/requiredStar.svelte';
</script>

<label class="agreement-label">
	<h4>Important Notice: <RequiredStar /></h4>
	<p>
		It is the responsibility of authors to obtain any required government or company reviews and/or
		clearances of their paper prior to submission, as well as any necessary reprinting permissions.
	</p>
	<input type="checkbox" required />
	Paper can be published
</label>

<style>
	.agreement-label {
		margin-bottom: 30px;
	}
	h4 {
		font-weight: normal;
	}
	input,
	p {
		margin-left: 20px;
	}
</style>
