<script>
	import { onMount } from 'svelte';
	import { countries } from 'countries-list';

	export let data;
	const countryCodes = Object.keys(countries);
	const countryNames = countryCodes.map((code) => countries[code].name);

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
			surname: '',
			email: '',
			country: '',
			affilation: '',
			web_page: '',
			is_presenter: false
		});
		authors = authors;
	}
	onMount(async () => {
		addAuthor();
		addAuthor();
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
	}
</script>

<svelte:head>
	<title>Submission {conferenceData.name}</title>
	<meta name="description" content="Home" />
</svelte:head>
<div class="container">
	{#if is_ru == true}
		<h3>{conferenceData.name_ru}</h3>
	{:else}
		<h3>{conferenceData.name}</h3>
	{/if}
	{#if conferenceData.allow_ru}
		<div>
			Choose submission language*
			<select
				required
				on:change={(element) => {
					is_ru = element.target.value == 'Russian';
					console.log(is_ru);
				}}
			>
				<option value="" disabled selected>Language</option>

				<option value="English">English</option>
				<option value="Russian">Russian</option>
			</select>
		</div>
	{/if}
	{#if is_ru == true}
		<div class="form-wrapper">
			<form class="ru-form" id="submission" on:submit={handleOnSubmit} method="POST">
				<div class="authors-container">
					{#each authors as author}
						<article class="author-item ru_author">
							<label>
								Имя*
								<input
									type="text"
									on:input={(author.first_name = this.value)}
									placeholder="На русском"
									name="#{author.id}#_first_name_ru"
									required
									value={author.first_name}
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
								Фамилия*
								<input
									type="text"
									on:input={(author.last_name = this.value)}
									placeholder="На русском"
									name="#{author.id}#_last_name_ru"
									required
									value={author.last_name}
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
								Отчество
								<input
									type="text"
									on:input={(author.surname = this.value)}
									placeholder="На русском"
									name="#{author.id}#_surname_ru"
									value={author.surname}
								/>
								<input
									type="text"
									on:input={(author.surname = this.value)}
									placeholder="На английском"
									name="#{author.id}#_surname"
									value={author.surname}
								/>
							</label>
							<label>
								Электронная почта*
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
								Страна*
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
								Организация*
								<input
									type="text"
									on:input={(author.affilation = this.value)}
									placeholder="Организация"
									name="#{author.id}#_affilation"
									required
									value={author.affilation}
								/>
							</label>
							<label>
								Личная веб-страница
								<input
									type="text"
									on:input={(author.web_page = this.value)}
									placeholder="Личная веб-страница"
									name="#{author.id}#_web_page"
									value={author.web_page}
								/>
							</label>
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
							{#if author.id != 0}
								<input
									class="blue-button"
									type="button"
									on:click={deleteAuthor(author.id)}
									value="Удалить"
								/>
							{/if}
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
					<input type="text" placeholder="Название на русском языке" name="title_ru" required />
				</label>
				<label>
					Название на английском языке*
					<input type="text" placeholder="Название на английском языке" name="title" required />
				</label>

				<label>
					Аннотация на русском языке*
					<p><i>Абстракт не должен превышать 500 слов</i></p>
					<textarea
						on:keyup={handleAbstractChange}
						name="abstract_ru"
						placeholder="Аннотация на русском языке"
						form="submission"
						cols="30"
						rows="10"
					></textarea>
					<p>Количество слов: {abstractLength}</p>
				</label>
				<label>
					Аннотация на английском языке*
					<p><i>Не более 500 слов.</i></p>
					<textarea
						on:keyup={handleAbstractChange}
						placeholder="Аннотация на английском языке"
						name="abstract"
						form="submission"
						cols="30"
						rows="10"
					></textarea>
					<p>Количество слов: {abstractLength}</p>
				</label>
				<label>
					Ключевые слова на русском языке*
					<p>
						<i>Минимум 3 ключевых слова (фразы), по одному на строку. </i>
					</p>

					<textarea
						on:keypress={handleKeyWordsChange}
						placeholder="Ключевые слова на русском языке"
						name="keywords_ru"
						form="submission"
						cols="30"
						rows="10"
					></textarea>
					<p>Ключевые слова: {keywordsLength}</p>
				</label>
				<label>
					Ключевые слова на английском языке*
					<p>
						<i>Минимум 3 ключевых слова (фразы), по одному на строку. </i>
					</p>

					<textarea
						on:keypress={handleKeyWordsChange}
						placeholder="Ключевые слова на английском языке"
						name="keywords"
						form="submission"
						cols="30"
						rows="10"
					></textarea>
					<p>Ключевые слова: {keywordsLength}</p>
				</label>

				<label>
					Направления*
					<p><i>Выберите предпочитаемое направлание</i></p>
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
					<select name="presentation_format">
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
			<form id="submission" on:submit={handleOnSubmit} method="POST">
				<div class="authors-container">
					{#each authors as author}
						<article class="author-item">
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
								Surname
								<input
									type="text"
									on:input={(author.surname = this.value)}
									placeholder="Surname"
									name="#{author.id}#_surname"
									value={author.surname}
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
									placeholder="Country"
									name="#{author.id}#_country"
									on:change={(author.country = this.value)}
								>
									<option value="" selected disabled>Country</option>
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
									placeholder="Affiliation"
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
									placeholder="Web page"
									name="#{author.id}#_web_page"
									value={author.web_page}
								/>
							</label>
							<label class="is_presenter-label">
								Presenter
								<input
									type="checkbox"
									on:input={(author.is_presenter = this.checked)}
									placeholder="Is presenter"
									name="#{author.id}#_is_presenter"
									value={author.is_presenter}
								/>
							</label>
							<input
								class="blue-button"
								type="button"
								on:click={deleteAuthor(author.id)}
								value="Delete"
							/>
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
						on:change={handleAbstractChange}
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
						on:change={handleKeyWordsChange}
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
					<select name="presentation_format">
						<option selected disabled>Choose</option>
						<option value="online">Online</option>
						<option value="offline">On-Sight</option>
					</select>
				</label>

				<input class="blue-button submit-button" type="submit" value="Submit" />
			</form>
		</div>
	{/if}
</div>

<style>
	.add_new_author-button,
	.submit-button {
		width: 200px;
	}
	.authors-container {
		display: flex;
		gap: 20px;
		flex-wrap: wrap;
		justify-content: space-evenly;
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
		width: 250px;
	}
	.author-item {
		min-width: 400px;
	}
	.ru_author > label {
		display: flex;
		flex-direction: column;
	}
	.is_presenter-label {
		width: 100%;
		align-items: center;
		justify-content: center !important;
		flex-direction: row !important;
	}
</style>
