<script>
	export let data;
</script>

<svelte:head>
	<title>Edit profile</title>
	<meta name="description" content="Registration page" />
</svelte:head>

<div class="container">
	<div class="form-wrapper">
		<form method="POST">
			<label>
				First name*
				<input
					type="text"
					placeholder="First name"
					name="first_name"
					required
					value={data.profile.first_name}
				/>
			</label>
			<label>
				Last name*
				<input
					type="text"
					placeholder="Last name"
					name="last_name"
					required
					value={data.profile.last_name}
				/>
			</label>
			<label>
				Surname
				<input type="text" placeholder="Surname" name="surname" value={data.profile.surname} />
			</label>
			<label>
				Affilation*
				<input
					type="text"
					placeholder="Affilation"
					required
					name="affilation"
					value={data.profile.affilation}
				/>
			</label>
			<label>
				Web page
				<input type="text" placeholder="Web page" name="web_page" value={data.profile.web_page} />
			</label>
			<label>
				Address line 1
				<input
					type="text"
					placeholder="Address line 1"
					name="address_line_1"
					value={data.profile.address_line_1}
				/>
			</label>
			<label>
				Address line 2
				<input
					type="text"
					placeholder="Address line 2"
					name="address_line_2"
					value={data.profile.address_line_2}
				/>
			</label>
			<label>
				City*
				<input type="text" placeholder="City" name="city" required value={data.profile.city} />
			</label>
			<label>
				State
				<input type="text" placeholder="State" name="state" value={data.profile.state} />
			</label>
			<label>
				Country*
				<input
					type="text"
					placeholder="Country"
					name="country"
					required
					value={data.profile.country}
				/>
			</label>
			<input class="blue-button floating-button" type="submit" value="Edit" />
		</form>
	</div>
</div>

<style>
	.form-wrapper {
		max-width: 400px;
		margin: auto;
	}
</style>
