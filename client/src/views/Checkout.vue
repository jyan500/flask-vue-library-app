<template>
	<div>
		<h2>Checkout </h2>	
		<b-row>
			<alert v-show = "message != ''" :message = "message" :is_success = "is_success"></alert>
		</b-row>
		<b-row>
			<b-col>
				<cart :is_view = "true" :is_checkout = "true"></cart>
			</b-col>
		</b-row>	
		<b-row>
			<b-col>
				<span><strong>Please enter the following information: </strong></span>
			</b-col>
		</b-row>
		<b-row>
			<b-col md = "2">
				<b-form @submit = "onSubmit">
					<b-form-group id = "library_card_num" label-for = "library_card_num" label = "Library Card">
						<b-form-input id = "library_card_num" v-model = "form.library_card_num"></b-form-input>
					</b-form-group>
					<b-form-group>
						<b-button type = "submit" variant = "primary">Submit</b-button>
					</b-form-group>
				</b-form>
			</b-col>
		</b-row>
	</div>
</template>
<style>
	
</style>
<script>
	import Alert from '../components/Alert.vue';
	import Cart from '../components/Cart.vue'
	import { EventBus } from '@/utils'
	export default {
		components : {
			cart : Cart,
			alert : Alert
		},
		props : {

		},
		data(){
			return {
				message : '',
				is_success : true,
				form : {
					library_card_num : '',
				}
			}
		},	
		mounted(){
			EventBus.$on('failedLibCardCheck', (msg) => {
				this.message = msg;
				this.is_success = false;
			})
		},
		methods : {
			onSubmit(evt){
				evt.preventDefault()
				this.message = '';
				this.$store.dispatch('checkout', this.form).then(
					(response) => {
						// clear the cart
						this.$store.dispatch('emptyCart');

						// redirect to the books page
						this.$router.push({name : 'Books', params : {message : response.data.message}})
					},
				).catch((error) => {
					console.log(error)
				})

			},
		}
	}	
</script>