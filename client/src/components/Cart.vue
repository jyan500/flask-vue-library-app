<template>
	<div>
		<table v-if = "cart.length > 0">
			<tbody>
				<tr :key = "book.library_book_id" v-for = "book in cart">
					<td>{{book.title}}</td>	
					<td>{{book.library}}</td>	
					<td>
						<b-button @click = "removeFromCart(book)">Remove From Cart</b-button>
					</td>	
				</tr>				
			</tbody>
		</table>
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
			removeFromCart(book){
				this.$store.dispatch('removeFromCart', book)
			}
		}
	}	
</script>