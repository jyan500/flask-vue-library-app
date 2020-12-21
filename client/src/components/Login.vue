<template>
	<b-container>
		<b-row>
			<alert v-show = "message != ''" :message = "message" :is_success = "is_success"></alert>
		</b-row>
		<b-row>
			<b-col>
				<b-form @submit = "onSubmit">
					<b-form-group id = "input-group-1" label = "Email Address" label-for = "input-1">
						<b-form-input id = "input-1" v-model = "form.email" type = "email" required placeholder = "Enter email">
						</b-form-input>
					</b-form-group>
					<b-form-group id = "input-group-2" label = "Password" label-for = "input-2">
						<b-form-input id = "input-2" v-model = "form.password" type = "password" required placeholder = "Enter password">
							
						</b-form-input>	
					</b-form-group>
					<b-button type = "submit" variant = "primary">Submit</b-button>
				</b-form>
			</b-col>	
		</b-row>
	</b-container>
</template>
<style>
	
</style>
<script>
	import Alert from './Alert.vue';
	import { EventBus } from '@/utils'
	export default {
		props : {

		},
		components : {
			alert : Alert	
		},
		data(){
			return {
				is_success : true,
				message : '',
				form : {
					email : '',
					password : '',
				}
			}
		},
		mounted(){
			
			EventBus.$on('failedAuthentication', (msg) => {
				this.message = msg;
			})
		},
		beforeDestroy(){
			EventBus.$off('failedAuthentication')
		},
		methods : {
			authenticate(){
				this.$store.dispatch('login', {email: this.form.email, password: this.form.password}).then(
					() => {
						this.$router.push('/')
					},
					(error) => {
						this.is_success = false;
						this.message = error.response.data.message;
					}
				)
			},
			onSubmit(evt){
				evt.preventDefault();
				this.is_success = true
				this.authenticate()
			}
		}
	}	
</script>
