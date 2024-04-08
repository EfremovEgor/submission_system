<script>
	import Agreement from './components/agreement.svelte';
	import RequiredStar from './../../formComponents/requiredStar.svelte';
	import AuthorPanel from './components/authorPanel.svelte';
	import AfterwordsInfo from './components/afterwordsInfo.svelte';
	import CounterKeywordsTextArea from './../../formComponents/counterKeywordsTextArea.svelte';
	import CounterTextArea from './../../formComponents/counterTextArea.svelte';
	import CounterTextInput from './../../formComponents/counterTextInput.svelte';
	import FormSection from './../../formComponents/formSection.svelte';
	import AuthorInfo from './components/authorInfo.svelte';
	import { enhance } from '$app/forms';
	import { countries } from 'countries-list';
	import { onMount } from 'svelte';

	export let userDetails;
	export let conferenceData;
	export let isBusy;
	export let sentEmail;

	const countryCodes = Object.keys(countries);
	const countryNames = countryCodes.map((code) => countries[code].name);

	let authors = [];
	let categories = {};
	let presentationFormat = null;
	let wordCountTitle = 0;
	let wordCountTitleRU = 0;
	let wordCountAbstract = 0;
	let wordCountAbstractRU = 0;
	let keywordsCount = 0;
	let keywordsCountRU = 0;
	conferenceData.topics.forEach((element) => {
		if (categories[element.category] == undefined) categories[element.category] = [element];
		else categories[element.category].push(element);
	});
	function handlePresentationFormatChange(event) {
		presentationFormat = event.target.value;
	}
	function handleOnSubmit(event) {}
	function deleteAuthor(id) {
		let new_authors = [];
		for (let author of authors) {
			if (author.id != id) new_authors.push(author);
		}
		authors = new_authors;
	}
	function addAuthor() {
		authors.push({
			id: authors.length,
			title: '',
			first_name: '',
			last_name: '',
			first_name_ru: '',
			last_name_ru: '',
			surname: '',
			surname_ru: '',
			email: '',
			country: '',
			affilation: '',
			affilation_ru: '',
			web_page: '',
			is_presenter: false,
			is_corresponding: false
		});
		authors = authors;
	}
	onMount(async () => {
		addAuthor();
		addAuthor();
	});
</script>

<div class="form-wrapper">
	<AuthorInfo />
	<form
		id="submission"
		on:submit={handleOnSubmit}
		method="POST"
		use:enhance={({ formElement, formData, action, cancel }) => {
			let error = false;
			if (wordCountTitleRU > 50) {
				error = true;
				alert('Title should not exceed 50 words');
			}

			if (wordCountAbstractRU > 500) {
				error = true;
				alert('Abstract should not exceed 500 words');
			}
			if (wordCountTitle > 50) {
				error = true;
				alert('Title should not exceed 50 words');
			}
			if (keywordsCount < 3) {
				error = true;
				alert('You should specify at least three keywords');
			}
			if (wordCountAbstract > 500) {
				error = true;
				alert('Abstract should not exceed 500 words');
			}
			if (authors.length == 0) {
				error = true;
				alert('Please add at least one author');
			}
			if (presentationFormat == null) {
				error = true;
				alert('Please choose presentation format');
			}
			if (error) {
				cancel();
				return;
			}
			isBusy = true;
			return async ({ result }) => {
				if (result.data.status == 200) {
					sentEmail = true;
					isBusy = false;
					return;
				}
			};
		}}
	>
		<div class="authors-container">
			{#each authors as author}
				<AuthorPanel {countryNames} {userDetails} {author} {deleteAuthor} />
			{/each}
		</div>
		<input
			class="blue-button add_new_author-button"
			type="button"
			on:click={addAuthor}
			value="Добавить авторов"
		/>
		<FormSection
			sectionHeading="Название и аннотация"
			sectionText="Аннотации должны быть написаны открытым текстом и не должны содержать таблиц, рисунков, фотографий, или элементов HTML."
		>
			<svelte:fragment slot="inputs">
				<label class="form_input-container" for="title_ru">
					<span class="form_input-label">Название на рус.:<RequiredStar /></span>
					<CounterTextInput
						bind:wordCount={wordCountTitleRU}
						placeholder="Не более 30 слов"
						name="title_ru"
					/>
				</label>
				<label class="form_input-container" for="title">
					<span class="form_input-label">Название на англ.:<RequiredStar /></span>
					<CounterTextInput
						bind:wordCount={wordCountTitle}
						placeholder="Не более 30 слов"
						name="title"
					/>
				</label>
				<label class="form_input-container" for="abstract_ru">
					<span class="form_input-label">Аннотация на рус.:<RequiredStar /></span>
					<CounterTextArea
						bind:wordCount={wordCountAbstractRU}
						name="abstract_ru"
						form="submission"
						placeholder="Не более 500 слов"
					/>
				</label>
				<label class="form_input-container" for="abstract">
					<span class="form_input-label">Аннотация на англ.:<RequiredStar /></span>
					<CounterTextArea
						bind:wordCount={wordCountAbstract}
						name="abstract"
						form="submission"
						placeholder="Не более 500 слов"
					/>
				</label>
			</svelte:fragment>
		</FormSection>

		<FormSection
			sectionHeading="Ключевые слова"
			sectionText="Введите ключевые слова (также известные как ключевые фразы, или ключевые термины), по одному в строку. Необходимо ввести не менее трех ключевых слов. "
		>
			<svelte:fragment slot="inputs">
				<label class="form_input-container" for="keywords">
					<span class="form_input-label">Ключевые слова на рус.:<RequiredStar /></span>
					<CounterKeywordsTextArea
						bind:wordCount={keywordsCount}
						name="keywords"
						form="submission"
						placeholder="Не менее трех ключевых слов. По одному в строке"
					/>
				</label>
				<label class="form_input-container" for="keywords_ru">
					<span class="form_input-label">Ключевые слова на англ.:<RequiredStar /></span>
					<CounterKeywordsTextArea
						bind:wordCount={keywordsCount}
						name="keywords_ru"
						form="submission"
						placeholder="Не менее трех ключевых слов. По одному в строке"
					/>
				</label>
			</svelte:fragment>
		</FormSection>

		<FormSection
			sectionHeading="Направления"
			required
			sectionText="Выберите предпочтительное направления для доклада."
		>
			<svelte:fragment slot="inputs">
				<fieldset>
					{#each Object.keys(categories) as category}
						<legend><b>{category}</b></legend>
						{#each categories[category] as topic}
							<label>
								<input type="radio" value={topic.id} name="topic" />
								{topic.name_ru}
							</label>
						{/each}
					{/each}
				</fieldset>
			</svelte:fragment>
		</FormSection>
		<label class="presentation_format-container">
			<h4>Формат доклада<RequiredStar /></h4>

			<select on:change={handlePresentationFormatChange} name="presentation_format">
				<option selected disabled>Выбрать</option>
				<option value="online">Заочный(Онлайн)</option>
				<option value="on-sight">Очный</option>
			</select>
		</label>
		<Agreement />
		<AfterwordsInfo />
		<input class="blue-button submit-button" type="submit" value="Submit" />
	</form>
</div>

<style>
	label > h4 {
		font-weight: normal;
	}
	.presentation_format-container {
		display: flex;
		align-items: center;
		gap: 20px;
	}
	.presentation_format-container > select {
		width: 200px;
	}
	.presentation_format-container > h4 {
		white-space: nowrap;
	}
	.add_new_author-button,
	.submit-button {
		min-width: 200px;
		width: fit-content;
	}
	.authors-container {
		display: flex;
		gap: 20px;
		flex-wrap: wrap;
	}

	.form_input-label {
		min-width: 250px;
		white-space: nowrap;
	}
	.form_input-container {
		display: flex;
		flex-direction: row;
		align-items: center;
		gap: 20px;
	}

	@media only screen and (max-width: 780px) {
		.form_input-container {
			flex-direction: column;
		}
		.form_input-label {
			text-align: center;
		}
	}
</style>
