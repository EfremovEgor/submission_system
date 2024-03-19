<script>
	import Agreement from './components/agreement.svelte';
	import RequiredStar from './../../formComponents/requiredStar.svelte';
	import AuthorPanel from './components/authorPanel.svelte';
	import AfterwordsInfo from './components/afterwordsInfo.svelte';
	import CounterKeywordsTextArea from '../../formComponents/counterKeywordsTextArea.svelte';
	import CounterTextArea from '../../formComponents/counterTextArea.svelte';
	import CounterTextInput from '../../formComponents/counterTextInput.svelte';
	import FormSection from '../../formComponents/formSection.svelte';
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
	let wordCountAbstract = 0;
	let keywordsCount = 0;
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
	<form
		id="submission"
		on:submit={handleOnSubmit}
		method="POST"
		use:enhance={({ formElement, formData, action, cancel }) => {
			let error = false;
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
		<AuthorInfo />
		<div class="authors-container">
			{#each authors as author}
				<AuthorPanel {authors} {countryNames} {userDetails} {author} {deleteAuthor} />
			{/each}
		</div>
		<input
			class="blue-button add_new_author-button"
			type="button"
			on:click={addAuthor}
			value="Add more authors"
		/>

		<FormSection
			sectionHeading="Title and Abstract"
			sectionText="Abstracts must be written in plain text and must not contain tables, figures,
        photographs or HTML elements."
		>
			<svelte:fragment slot="inputs">
				<label class="form_input-container" for="title">
					<span class="form_input-label">Title:<RequiredStar /></span>
					<CounterTextInput
						bind:wordCount={wordCountTitle}
						placeholder="Not more than 30 words"
						name="title"
					/>
				</label>
				<label class="form_input-container" for="abstract">
					<span class="form_input-label">Abstract:<RequiredStar /></span>
					<CounterTextArea
						bind:wordCount={wordCountAbstract}
						name="abstract"
						form="submission"
						placeholder="Not more than 500 words"
					/>
				</label>
			</svelte:fragment>
		</FormSection>

		<FormSection
			sectionHeading="Keywords"
			sectionText="Type a list of keywords (also known as key phrases or key terms), one per line
        to characterize your submission. You should specify at least three keywords."
		>
			<svelte:fragment slot="inputs">
				<label class="form_input-container" for="keywords">
					<span class="form_input-label">Keywords:<RequiredStar /></span>
					<CounterKeywordsTextArea
						bind:wordCount={keywordsCount}
						name="keywords"
						form="submission"
						placeholder="Not less than 3 keywords. One per line"
					/>
				</label>
			</svelte:fragment>
		</FormSection>
		<FormSection
			sectionHeading="Topics"
			required
			sectionText="Choose preferable topic for your paper."
		>
			<svelte:fragment slot="inputs">
				<fieldset>
					{#each Object.keys(categories) as category}
						<legend><b>{category}</b></legend>
						{#each categories[category] as topic}
							<label>
								<input type="radio" value={topic.id} required name="topic" />
								{topic.name}
							</label>
						{/each}
					{/each}
				</fieldset>
			</svelte:fragment>
		</FormSection>
		<label class="presentation_format-container">
			<h4>Presentation format<RequiredStar /></h4>

			<select on:change={handlePresentationFormatChange} name="presentation_format">
				<option selected disabled>Choose</option>
				<option value="online">Online</option>
				<option value="on-sight">On-Sight</option>
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
		min-width: 100px;
		white-space: nowrap;
	}
	.form_input-container {
		display: flex;
		min-width: fit-content;
		flex-direction: row;
		gap: 20px;
		align-items: center;
	}
	.presentation_format-container > select {
		width: 200px;
	}
	@media only screen and (max-width: 780px) {
		.form_input-container {
			flex-direction: column;
		}
		.presentation_format-container {
			gap: 0px;
			flex-direction: column;
		}
	}
</style>
