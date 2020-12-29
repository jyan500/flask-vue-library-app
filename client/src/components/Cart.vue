<template>
	<div>
		<b-list-group v-if = "cart.length > 0">
			<b-list-group-item :key = "book.id" v-for = "book in cart">
				{{ book.title }}	
			</b-list-group-item>		
		</b-list-group>	
		<span v-else>The cart is empty</span>
	</div>
</template>
<style>
	
</style>
<script>
	export default {
		props : {

		},
		data(){
			return {

			}
		},
		computed : {
			cart(){
				return this.$store.getters.getCart
			},
		},
		methods : {

		}
	}	
</script>