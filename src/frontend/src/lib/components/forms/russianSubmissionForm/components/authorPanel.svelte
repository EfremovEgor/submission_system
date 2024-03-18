<script>
	import RequiredStar from './../../../formComponents/requiredStar.svelte';
	import Icon from '@iconify/svelte';

	export let userDetails;
	export let author;
	export let deleteAuthor;
	export let countryNames;
	if (author.id == 0) {
		author.is_corresponding = true;
		author.is_presenter = true;
	}
	function handleFillAuthorForm(id) {
		author.first_name = userDetails.first_name;
		author.title = userDetails.title;
		author.last_name = userDetails.last_name;
		author.surname = userDetails.surname;
		author.email = userDetails.email;
		author.country = userDetails.country;
		author.affilation = userDetails.affilation;
		author.web_page = userDetails.web_page;
	}
</script>

<article class="author-item ru_author">
	<div class="author-header">
		<div class="author_heading-container">
			<h4 class="author-heading">Автор {author.id + 1}</h4>
			<div class="fill_form-button-container">
				<span
					on:click={handleFillAuthorForm(author.id)}
					on:keydown={handleFillAuthorForm(author.id)}
					class="link fill_form-button">Заполнить собственными данными</span
				>
			</div>
		</div>

		{#if author.id != 0}
			<button on:click={deleteAuthor(author.id)} class="icon-button icon-button_close"
				><Icon class="icon" icon="material-symbols-light:close" /></button
			>
		{/if}
	</div>
	<label class="prefix_field-container">
		<span>Префикс:<RequiredStar /></span>
		<select
			required
			placeholder="Choose"
			name="#{author.id}#_title"
			on:change={(author.title = this.value)}
		>
			<option value="" selected disabled>Выбрать</option>
			<option value="Mr.">Mr.</option>
			<option value="Mrs.">Mrs.</option>
			<option value="Ms.">Ms.</option>
			<option value="Dr.">Dr.</option>
			<option value="Prof.">Prof.</option>
		</select>
	</label>
	<label>
		<span>Фамилия:<RequiredStar /></span>
		<input
			type="text"
			on:input={(author.last_name_ru = this.value)}
			placeholder="На русском"
			name="#{author.id}#_last_name_ru"
			required
			value={author.last_name_ru}
		/>
		<input
			type="text"
			on:input={(author.last_name = this.value)}
			placeholder="На английском"
			name="#{author.id}#_last_name"
			required
			value={author.last_name}
		/>
	</label>
	<label>
		<span>Имя:<RequiredStar /></span>
		<input
			type="text"
			on:input={(author.first_name_ru = this.value)}
			placeholder="На русском"
			name="#{author.id}#_first_name_ru"
			required
			value={author.first_name_ru}
		/>
		<input
			type="text"
			on:input={(author.first_name = this.value)}
			placeholder="На английском"
			name="#{author.id}#_first_name"
			required
			value={author.first_name}
		/>
	</label>

	<label>
		<span>Отчество:</span>
		<input
			type="text"
			on:input={(author.surname_ru = this.value)}
			placeholder="На русском"
			name="#{author.id}#_surname_ru"
			value={author.surname_ru}
		/>
	</label>
	<label>
		<span>Электронная почта:<RequiredStar /></span>
		<input
			type="email"
			on:input={(author.email = this.value)}
			placeholder="Электронная почта"
			name="#{author.id}#_email"
			required
			value={author.email}
		/>
	</label>
	<label>
		<span>Страна:<RequiredStar /></span>
		<select
			required
			placeholder="Country"
			name="#{author.id}#_country"
			on:change={(author.country = this.value)}
		>
			<option value="" selected disabled>Выбрать</option>
			{#each countryNames as country}
				<option value={country}>{country}</option>
			{/each}
		</select>
	</label>
	<label>
		<span>Организация:<RequiredStar /></span>
		<input
			type="text"
			on:input={(author.affilation_ru = this.value)}
			placeholder="На русском"
			name="#{author.id}#_affilation_ru"
			required
			value={author.affilation_ru}
		/>
		<input
			type="text"
			on:input={(author.affilation = this.value)}
			placeholder="На английском"
			name="#{author.id}#_affilation"
			required
			value={author.affilation}
		/>
	</label>
	<label>
		<span>Личная веб-страница:</span>
		<input
			type="text"
			on:input={(author.web_page = this.value)}
			placeholder="URL"
			name="#{author.id}#_web_page"
			value={author.web_page}
		/>
	</label>
	<div class="author_checkbox-container">
		<label class="is_corresponding-label">
			Контактное лицо
			<input
				checked={author.id == 0}
				type="checkbox"
				on:input={(event) => {
					author.is_corresponding = event.target.checked;
				}}
				name="#{author.id}#_is_corresponding"
				value={author.is_corresponding}
			/>
		</label>
		<label class="is_presenter-label">
			Докладчик
			<input checked={author.id == 0} type="radio" value={author.id} name="is_presenter" />
		</label>
	</div>
</article>

<style>
	.author-item {
		padding: 20px;
	}
	.author-item > label {
		display: grid;
		align-items: center;
		grid-template-columns: repeat(3, 1fr);
		gap: 30px;
	}
	.author-item > label > * {
		width: 200px;
	}
	.author-item {
		min-width: 400px;
	}
	@media only screen and (max-width: 780px) {
		.author-item > label {
			display: flex;
			flex-direction: column;
			gap: 0px;
		}
		.author-item > label > * {
			width: 90%;
		}
		.author-item {
			min-width: 300px;
		}
	}

	.is_presenter-label,
	.is_corresponding-label {
		width: 100%;
		align-items: center;
		justify-content: center;
		flex-direction: row;
	}

	.fill_form-button-container {
		width: 100%;
		display: flex;
		justify-content: center;
		margin-bottom: 10px;
		font-size: small;
	}
	.author-heading {
		text-align: center;
		margin-bottom: 0px;
	}
	.author_checkbox-container {
		width: 100%;
		display: flex;
		flex-direction: column;
	}
	.author_checkbox-container > label {
		display: flex;
		justify-content: end !important;
		align-items: center;
		gap: 20px;
	}
	.author-header {
		display: flex;
		justify-content: space-between;
		flex-direction: row;
	}
	.author_heading-container {
		display: flex;
		flex-direction: column;
		justify-content: center;
		width: 100%;
	}
	.prefix_field-container {
		display: flex !important;
		justify-content: space-between;
	}
</style>
