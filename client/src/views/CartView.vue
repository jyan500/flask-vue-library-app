<template>
	<div>
		<h2>Your Cart</h2>
		<hr/>
		<b-row class = "mt-3 mb-3">
			<b-col>
				<cart :is_view = "true"></cart>
			</b-col>
		</b-row>
		<b-row class = "mt-3 mb-3">
			<b-col>
				<div v-if = "amountInCart > 0">
					<b-button v-if = "isAuthenticated" to = "/checkout">Continue to Checkout</b-button>
					<span v-else>Please <b-link to = '/login'>Login</b-link> to your account to checkout</span>
				</div>
				<div v-else>
					Please add items to cart before checking out
				</div>
			</b-col>
		</b-row>
	</div>	
</template>
<style>
	
</style>
<script>
	import Cart from '../components/Cart.vue'
	export default {
		components : {
			cart : Cart
		},
		data(){
			return { 

			}
		},	
		computed : {
			isAuthenticated(){
				return this.$store.getters.isAuthenticated	
			},
			amountInCart(){
				return this.$store.getters.getCart.length
			},
		},
		methods : {

		}
	}
</script>