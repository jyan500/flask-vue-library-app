<template>
	<b-navbar toggleable = "lg" type = "dark" variant = "info">
		<b-navbar-brand to = "/">San Mateo County Library</b-navbar-brand>	
		<b-navbar-toggle target = "nav-collapse"></b-navbar-toggle>
		<b-collapse id = "nav-collapse" is-nav>
			<b-navbar-nav>
				<b-nav-item v-if = "!isAuthenticated" to ="/login">Login</b-nav-item>
				<b-nav-item v-if = "!isAuthenticated" to = "/register">Register</b-nav-item>
				<b-nav-item to = "/catalog">Catalog</b-nav-item>
				<b-nav-item v-if = "isAuthenticated" to = "/books">Books</b-nav-item>
				<b-nav-item v-if = "isAuthenticated" @click = "logout">Logout</b-nav-item>
			</b-navbar-nav>	
		</b-collapse>
	</b-navbar>	
</template>
<style>
</style>
<script>

	export default {
		computed : {
			isAuthenticated(){
				return this.$store.getters.isAuthenticated	
			}
		},
		methods : {
			logout(){
				this.$store.dispatch('logout').then(
					(response) => {
						this.$router.push({'name' : 'Home', params : {message : response.data.message}})
					},
				)
			},
		}	
	}
</script>
