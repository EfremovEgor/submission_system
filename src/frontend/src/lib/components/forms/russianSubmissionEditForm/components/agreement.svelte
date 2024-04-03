<script>
	import RequiredStar from '../../../formComponents/requiredStar.svelte';
</script>

<label class="agreement-label">
	<h4>Важно<RequiredStar /></h4>
	<p>
		Авторы несут ответственность за все необходимые проверки перед подачей доклада и/или получение
		разрешений правительства или компании на публикацию аннотации доклада и статьи в открытых
		источниках.
	</p>
	<input type="checkbox" required />
	Подтверждаю, что моя статья может быть опубликована
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
