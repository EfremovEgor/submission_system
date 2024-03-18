<script>
	import RequiredStar from './../../../lib/components/formComponents/requiredStar.svelte';
	export let data;

	import { countries } from 'countries-list';
	const countryCodes = Object.keys(countries);
	const countryNames = countryCodes.map((code) => countries[code].name);
	let country;
</script>

<svelte:head>
	<title>Edit profile</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	<div class="form-wrapper">
		<form method="POST">
			<label class="input-label">
				<span>First name <RequiredStar /></span>
				<input
					type="text"
					placeholder="First name"
					name="first_name"
					required
					value={data.profile.first_name}
				/>
			</label>
			<label class="input-label">
				<span>Last name <RequiredStar /></span>
				<input
					type="text"
					placeholder="Last name"
					name="last_name"
					required
					value={data.profile.last_name}
				/>
			</label>
			<label class="input-label">
				<span>Surname</span>
				<input type="text" placeholder="Surname" name="surname" value={data.profile.surname} />
			</label>
			<label class="input-label">
				<span>Affiliation<RequiredStar /></span>
				<input
					type="text"
					placeholder="Affiliation"
					name="affilation"
					required
					value={data.profile.affilation}
				/>
			</label>

			<label class="input-label">
				<span>Country<RequiredStar /></span>
				<select required placeholder="Choose" name="country" on:change={(country = this.value)}>
					{#each countryNames as country}
						<option selected={country === data.profile.country} value={country}>{country}</option>
					{/each}
				</select>
			</label>
			<label class="input-label">
				<span>City</span>
				<input type="text" placeholder="City" name="city" value={data.profile.city} />
			</label>
			<label class="input-label">
				<span>State</span>
				<input type="text" placeholder="State" name="state" value={data.profile.state} />
			</label>

			<label class="input-label">
				<span>ORCID ID</span>
				<input type="text" placeholder="ORCID ID" name="orcid_id" value={data.profile.orcid_id} />
			</label>
			<label class="input-label">
				<span>Web page</span>
				<input type="text" placeholder="Web page" name="web_page" value={data.profile.web_page} />
			</label>
			<input class="blue-button floating-button submit-button" type="submit" value="Edit" />
		</form>
	</div>
</div>

<style>
	.submit-button {
		max-width: 200px;
	}
	.input-label {
		display: flex;
		align-items: center;
		gap: 20px;
		margin-bottom: 20px;
	}
	.input-label > input {
		max-width: 200px;
	}
	.input-label > span {
		white-space: nowrap;
		min-width: 120px;
	}
	.input-label > input,
	select {
		margin-bottom: 0px;
		max-width: 200px;
	}
	.form-wrapper {
		margin: auto;
		width: fit-content;
	}
	.form-wrapper > form {
		display: flex;
		flex-direction: column;
		align-items: center;
		max-width: 500px;
	}
</style>
