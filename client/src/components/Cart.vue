<template>
	<div>
		<div v-if = "!is_view">
			<table v-if = "cart.length > 0">
				<tbody>
					<tr :key = "book.library_book_id" v-for = "book in cart">
						<td>{{book.title}}</td>	
						<td>{{book.library}}</td>	
						<td>
							<i @click = "removeFromCart(book)" class = "fas fa-trash"></i>
						</td>	
					</tr>				
				</tbody>
			</table>
			<span v-else>The cart is empty</span>
		</div>
		<div v-else>
			<b-table v-if = "cart.length > 0" :items = "cart" :fields = "fields">
				<template v-if = "!is_checkout" #cell(action)="row"><i @click = "removeFromCart(row.item)" class = "fas fa-trash"></i></template>
			</b-table>
			<span v-else>The cart is empty</span>
		</div>
	</div>
</template>
<style>
	
</style>
<script>
	export default {
		props : {
			is_view : Boolean,
			is_checkout : {
				type : Boolean,
				default : false
			}
		},
		data(){
			return {
				fields : [{'key' : 'title', 'label' : 'Title'}, {'key' : 'library', 'label' : 'Library'}, {'key' : 'action', 'label' : ''}]
			}
		},
		computed : {
			cart(){
				return this.$store.getters.getCart
			},
		},
		methods : {
			removeFromCart(book){
				console.log('book: ', book)
				this.$store.dispatch('removeFromCart', book)
			}
		}
	}	
</script>