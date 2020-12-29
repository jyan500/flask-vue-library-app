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
			</b-navbar-nav>	
			<b-navbar-nav class="ml-auto">
				<b-nav-form>
					<b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
					<b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
				</b-nav-form>
				<b-nav-item id = "cart-popover" right>
					Cart
					<b-popover placement = "bottom" triggers = "hover focus" target = "cart-popover">
						<template #title>
							Cart
						</template>	
						<cart></cart>
					</b-popover>
				</b-nav-item>
				<b-nav-item-dropdown v-if = "isAuthenticated" right>
					<!-- Using 'button-content' slot -->
					<template #button-content>
						<em>User</em>
					</template>
					<b-dropdown-item href="#">Profile</b-dropdown-item>
					<b-dropdown-item @click = "logout">Logout</b-dropdown-item>
				</b-nav-item-dropdown>
			</b-navbar-nav>
		</b-collapse>
	</b-navbar>	
</template>
<style>
</style>
<script>
	import Cart from './Cart.vue'
	export default {
		components : {
			cart : Cart
		},
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
