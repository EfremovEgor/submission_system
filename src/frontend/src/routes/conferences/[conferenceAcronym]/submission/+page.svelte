<script>
	import { onMount } from 'svelte';
	import { countries } from 'countries-list';
	import { enhance } from '$app/forms';
	export let data;
	const userDetails = data.userDetails;
	const countryCodes = Object.keys(countries);
	const countryNames = countryCodes.map((code) => countries[code].name);
	let modal;
	let languageChoose;
	let isBusy = false;
	let sentEmail = false;

	let conferenceData = data.conference;
	let categories = {};
	conferenceData.topics.forEach((element) => {
		if (categories[element.category] == undefined) categories[element.category] = [element];
		else categories[element.category].push(element);
	});
	let authors = [];
	let abstractLength = 0;
	let keywordsLength = 0;
	let is_ru = null;
	let presentationFormat = null;
	function handleFillAuthorForm(id) {
		authors[id].first_name = userDetails.first_name;
		authors[id].last_name = userDetails.last_name;
		authors[id].surname = userDetails.surname;
		authors[id].email = userDetails.email;
		authors[id].country = userDetails.country;
		authors[id].affilation = userDetails.affilation;
		authors[id].web_page = userDetails.web_page;
	}
	function handlePresentationFormatChange(event) {
		presentationFormat = event.target.value;
		console.log(presentationFormat);
	}
	function handleAbstractChange(event) {
		abstractLength = event.target.value.trim().split(/\s+/).length;
	}
	function handleKeyWordsChange(event) {
		keywordsLength = event.target.value.split(/\r\n|\r|\n/).length;
	}
	function addAuthor() {
		authors.push({
			id: authors.length,
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
		if (!conferenceData.allow_ru || conferenceData.allow_ru == null) {
			is_ru = false;
		}
	});
	function deleteAuthor(id) {
		let new_authors = [];
		for (let author of authors) {
			if (author.id != id) new_authors.push(author);
		}
		authors = new_authors;
	}
	function handleOnSubmit(event) {
		if (keywordsLength < 3) {
			event.preventDefault();
			alert('You should specify at least three keywords');
			return;
		}
		if (abstractLength > 500) {
			event.preventDefault();
			alert('Abstract should not exceed 500 words');
			return;
		}
		if (authors.length == 0) {
			event.preventDefault();
			alert('Please add at least one author');
			return;
		}
		if (presentationFormat == null) {
			event.preventDefault();
			alert('Please choose presentation format');
			return;
		}
	}
</script>

<svelte:head>
	<title>Submission {conferenceData.name}</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	{#if isBusy}
		<article aria-busy="true">Please wait while we are processing your submission...</article>
	{:else if sentEmail}
		<article class="verification_sent-container">
			<h3>Your paper was successfully submitted</h3>
			<p>Please check your email.</p>
			<p>If you haven't recieved email, please check spam folder</p>
		</article>
	{:else}
		{#if conferenceData.allow_ru}
			<dialog bind:this={modal} open>
				<article class="modal">
					<header>
						<p>
							<strong>Please choose submission language</strong>
						</p>
					</header>
					<div class="modal-main">
						<select bind:this={languageChoose} required>
							<option value="" disabled selected>Language</option>

							<option value="English">English</option>
							<option value="Russian">Russian</option>
						</select>
					</div>
					<footer>
						<button
							class="button-error"
							on:click={(event) => {
								modal.open = false;
							}}>Cancel</button
						>
						<button
							class="button-success"
							on:click={(event) => {
								if (languageChoose.value == null) {
									alert('Please choose language');
									return;
								}
								console.log(languageChoose.value);
								is_ru = languageChoose.value == 'Russian';
								modal.open = false;
							}}>Confirm</button
						>
					</footer>
				</article>
			</dialog>
		{/if}

		{#if is_ru == true}
			<h3>{conferenceData.name_ru}</h3>
		{:else}
			<h3>{conferenceData.name}</h3>
		{/if}
		{#if is_ru == null}
			<button
				on:click={() => {
					modal.open = true;
				}}>Choose language</button
			>
		{/if}
		{#if is_ru == true}
			<div class="form-wrapper">
				<div>
					<p>Пожалуйста, заполните информацию ниже для каждого автора.</p>

					<p>
						Каждый автор, отмеченный как Контактное лицо, получит от системы электронное сообщение о
						подаче аннотации. Должен быть указан хотя бы один автор в качестве контактного лица.
					</p>

					<p>
						Один из авторов должен быть отмечен как Докладчик. Если вы не уверены в настоящий
						момент, сделайте наиболее вероятный выбор, это можно скорректировать позднее.
					</p>

					<p>
						Адреса электронных почт будут использоваться только для связи с авторами в рамках
						подаваемой аннотации. Электронные адреса не появятся на общедоступных веб-страницах
						конференции.
					</p>
				</div>
				<form
					class="ru-form"
					id="submission"
					on:submit={handleOnSubmit}
					method="POST"
					use:enhance={({ formElement, formData, action, cancel }) => {
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
							<article class="author-item ru_author">
								<div class="delete_author-container">
									{#if author.id != 0}
										<input
											class="blue-button delete_author-button"
											type="button"
											on:click={deleteAuthor(author.id)}
											value="⨯"
										/>
									{/if}
								</div>
								<h4 class="author-heading">Автор {author.id + 1}</h4>
								<div class="fill_form-button-container">
									<span
										on:click={handleFillAuthorForm(author.id)}
										on:keydown={handleFillAuthorForm(author.id)}
										class="link fill_form-button">Заполнить собственными данными</span
									>
								</div>
								<label>
									<span>Фамилия*</span>
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
									<span>Имя*</span>
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
									<span>Отчество</span>
									<input
										type="text"
										on:input={(author.surname_ru = this.value)}
										placeholder="На русском"
										name="#{author.id}#_surname_ru"
										value={author.surname_ru}
									/>
								</label>
								<label>
									<span>Электронная почта*</span>
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
									<span>Страна*</span>
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
									<span>Организация*</span>
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
									<span>Личная веб-страница</span>
									<input
										type="text"
										on:input={(author.web_page = this.value)}
										placeholder="URL"
										name="#{author.id}#_web_page"
										value={author.web_page}
									/>
								</label>
								<div class="author_checkbox-container">
									<label class="is_presenter-label">
										Докладчик
										<input
											type="checkbox"
											on:input={(author.is_presenter = this.checked)}
											placeholder="Is presenter"
											name="#{author.id}#_is_presenter"
											value={author.is_presenter}
										/>
									</label>
									<label class="is_corresponding-label">
										Контактное лицо
										<input
											type="checkbox"
											on:input={(author.is_corresponding = this.checked)}
											placeholder="Is corresponding"
											name="#{author.id}#_is_corresponding"
											value={author.is_corresponding}
										/>
									</label>
								</div>
							</article>
						{/each}
					</div>
					<input
						class="blue-button add_new_author-button"
						type="button"
						on:click={addAuthor}
						value="Добавить автора"
					/>
					<label>
						Название на русском языке*
						<input type="text" placeholder="Не более 30 слов" name="title_ru" required />
					</label>
					<label>
						Название на английском языке*
						<input type="text" placeholder="Не более 30 слов" name="title" required />
					</label>
					<label>
						Аннотация на русском языке*
						<textarea
							on:keyup={handleAbstractChange}
							name="abstract_ru"
							placeholder="Аннотация не более 500 слов"
							form="submission"
							cols="30"
							rows="10"
						></textarea>
						<p>Количество слов: {abstractLength}</p>
					</label>
					<label>
						Аннотация на английском языке*
						<textarea
							on:keyup={handleAbstractChange}
							placeholder="Не более 500 слов"
							name="abstract"
							form="submission"
							cols="30"
							rows="10"
						></textarea>
						<p>Количество слов: {abstractLength}</p>
					</label>
					<label>
						Ключевые слова на русском языке*

						<textarea
							on:keypress={handleKeyWordsChange}
							placeholder="Минимум 3 ключевых слова (фразы), по одному на строку"
							name="keywords_ru"
							form="submission"
							cols="30"
							rows="10"
						></textarea>
						<p>Ключевые слова: {keywordsLength}</p>
					</label>
					<label>
						Ключевые слова на английском языке*

						<textarea
							on:keypress={handleKeyWordsChange}
							placeholder="Минимум 3 ключевых слова (фразы), по одному на строку"
							name="keywords"
							form="submission"
							cols="30"
							rows="10"
						></textarea>
						<p>Ключевые слова: {keywordsLength}</p>
					</label>
					<label>
						<p><i>Выберите предпочитаемое направление*</i></p>
						<fieldset>
							{#each Object.keys(categories) as category}
								<legend><b>{category}</b></legend>
								{#each categories[category] as topic}
									<label>
										<input type="radio" value={topic.id} name="topic" />
										{topic.name}
									</label>
								{/each}
							{/each}
						</fieldset>
					</label>
					<label>
						Формат доклада*
						<select on:change={handlePresentationFormatChange} name="presentation_format">
							<option selected disabled>Выбрать</option>
							<option value="online">Заочный(Онлайн)</option>
							<option value="offline">Очный</option>
						</select>
					</label>

					<input class="blue-button submit-button" type="submit" value="Submit" />
				</form>
			</div>
		{:else if is_ru == false}
			<div class="form-wrapper">
				<div>
					<p>For each author please fill out forms below.</p>
					<p>
						Each author marked as a Corresponding author will receive email messages from the system
						about this submission. There must be at least one corresponding author.
					</p>
					<p>
						One of the authors should be marked as a Presenter. If you are not sure, make your best
						choice, it could be updated later.
					</p>
					<p>
						Email address will only be used for communication with the authors. It will not appear
						in public Web pages of this conference.
					</p>
				</div>
				<form
					id="submission"
					on:submit={handleOnSubmit}
					method="POST"
					use:enhance={({ formElement, formData, action, cancel }) => {
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
							<article class="author-item">
								<div class="delete_author-container">
									{#if author.id != 0}
										<input
											class="blue-button delete_author-button"
											type="button"
											on:click={deleteAuthor(author.id)}
											value="⨯"
										/>
									{/if}
								</div>
								<h4 class="author-heading">Author {author.id + 1}</h4>
								<div class="fill_form-button-container">
									<span
										on:click={handleFillAuthorForm(author.id)}
										on:keydown={handleFillAuthorForm(author.id)}
										class="link fill_form-button">Fill out with personal details</span
									>
								</div>
								<label>
									First name*
									<input
										type="text"
										on:input={(author.first_name = this.value)}
										placeholder="First name"
										name="#{author.id}#_first_name"
										required
										value={author.first_name}
									/>
								</label>
								<label>
									Last name*
									<input
										type="text"
										on:input={(author.last_name = this.value)}
										placeholder="Last name"
										name="#{author.id}#_last_name"
										required
										value={author.last_name}
									/>
								</label>

								<label>
									Email*
									<input
										type="email"
										on:input={(author.email = this.value)}
										placeholder="Email"
										name="#{author.id}#_email"
										required
										value={author.email}
									/>
								</label>
								<label>
									Country*
									<select
										required
										placeholder="Choose"
										name="#{author.id}#_country"
										on:change={(author.country = this.value)}
									>
										<option value="" selected disabled>Choose</option>
										{#each countryNames as country}
											<option value={country}>{country}</option>
										{/each}
									</select>
								</label>
								<label>
									Affiliation*
									<input
										type="text"
										on:input={(author.affilation = this.value)}
										placeholder="Organization"
										name="#{author.id}#_affilation"
										required
										value={author.affilation}
									/>
								</label>
								<label>
									Web page
									<input
										type="text"
										on:input={(author.web_page = this.value)}
										placeholder="URL"
										name="#{author.id}#_web_page"
										value={author.web_page}
									/>
								</label>
								<div class="author_checkbox-container">
									<label class="is_presenter-label">
										Presenter
										<input
											type="checkbox"
											on:input={(author.is_presenter = this.checked)}
											placeholder="Presenter"
											name="#{author.id}#_is_presenter"
											value={author.is_presenter}
										/>
									</label>
									<label class="is_corresponding-label">
										Corresponding Author
										<input
											type="checkbox"
											on:input={(author.is_corresponding = this.checked)}
											placeholder="Is corresponding"
											name="#{author.id}#_is_corresponding"
											value={author.is_corresponding}
										/>
									</label>
								</div>
							</article>
						{/each}
					</div>
					<input
						class="blue-button add_new_author-button"
						type="button"
						on:click={addAuthor}
						value="Add new author"
					/>
					<label>
						Title*
						<input type="text" placeholder="Title" name="title" required />
					</label>
					<label>
						Abstract*
						<p><i>The abstract should not exceed 500 words</i></p>
						<textarea
							on:keypress={handleAbstractChange}
							name="abstract"
							form="submission"
							cols="30"
							rows="10"
						></textarea>
						<p><b>Words: {abstractLength}</b></p>
					</label>
					<label>
						Keywords*
						<p>
							<i
								>Type a list of keywords (also known as key phrases or key terms), one per line to
								characterize your submission. You should specify at least three keywords.
							</i>
						</p>

						<textarea
							on:keypress={handleKeyWordsChange}
							name="keywords"
							form="submission"
							cols="30"
							rows="10"
						></textarea>
						<p><b>Keywords: {keywordsLength}</b></p>
					</label>
					<label>
						Topics*
						<fieldset>
							{#each Object.keys(categories) as category}
								<legend><b>{category}</b></legend>
								{#each categories[category] as topic}
									<label>
										<input type="radio" value={topic.id} name="topic" />
										{topic.name}
									</label>
								{/each}
							{/each}
						</fieldset>
					</label>
					<label>
						Presentation format*
						<select on:change={handlePresentationFormatChange} name="presentation_format">
							<option selected disabled>Choose</option>
							<option value="online">Online</option>
							<option value="offline">On-Sight</option>
						</select>
					</label>
					<input class="blue-button submit-button" type="submit" value="Submit" />
				</form>
			</div>
		{/if}
	{/if}
</div>

<style>
	.verification_sent-container {
		margin: auto;
		width: fit-content;
		min-height: 300px;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.verification_sent-container > h3 {
		color: rgb(71, 164, 23);
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
	.modal {
		width: fit-content;
	}
	.modal > footer {
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.modal > footer > button {
		min-width: 120px;
	}
	.modal-main {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.add_new_author-button,
	.submit-button {
		width: 200px;
	}
	.authors-container {
		display: flex;
		gap: 20px;
		flex-wrap: wrap;
	}
	.author-item {
		padding: 20px;
	}
	.author-item > label {
		display: flex;
		flex-direction: row;
		justify-content: space-between;
		align-items: center;
		gap: 20px;
	}
	.author-item > label > input,
	select {
		width: 200px;
	}
	.author-item {
		min-width: 400px;
	}
	.ru_author > label {
		display: flex;
		flex-flow: row;
	}

	.ru_author > label > * {
		width: 200px;
	}
	.is_presenter-label,
	.is_corresponding-label {
		width: 100%;
		align-items: center;
		justify-content: center !important;
		flex-direction: row !important;
	}
	.delete_author-button {
		width: 40px;
		padding: 0px;
		height: 40px;
		margin: 0;
	}

	.delete_author-container {
		display: flex;
		width: 100%;
		justify-content: end;
		min-height: 50px;
	}
</style>
