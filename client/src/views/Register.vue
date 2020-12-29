<template>
	<b-container>
		<b-row>
			<alert v-show = "message != ''" :message = "message" :is_success = "is_success"></alert>
		</b-row>
		<b-row>
			<b-col>
				<b-form @submit = "onSubmit">
					<b-form-group id = "input-group-1" label = "Firstname" label-for = "input-1">
						<b-form-input id = "input-1" v-model = "form.firstname" type = "text" required placeholder = "Enter your first name">
						</b-form-input>
					</b-form-group>
					<b-form-group id = "input-group-2" label = "Lastname" label-for = "input-2">
						<b-form-input id = "input-2" v-model = "form.lastname" type = "text" required placeholder = "Enter your last name">
							
						</b-form-input>	
					</b-form-group>
					<b-form-group id = "input-group-3" label = "Email Address" label-for = "input-3">
						<b-form-input id = "input-3" v-model = "form.email" type = "email" required placeholder = "Enter email">
						</b-form-input>
					</b-form-group>
					<b-form-group id = "input-group-4" label = "Password" label-for = "input-4">
						<b-form-input id = "input-4" v-model = "form.password" type = "password" required placeholder = "Enter password">
							
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
	import { EventBus } from '@/utils'
	import Alert from '../components/Alert.vue';
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
					firstname : '',
					lastname : '',
				}
			}
		},
		mounted(){
			EventBus.$on('failedRegistering', msg => {
				console.log('Failed Registration!')
				this.is_success = false;
				this.message = msg;
			})
		},
		beforeDestroy(){
			EventBus.$off('failedRegistering')
		},
		methods : {
			register(){
				this.$store.dispatch('register', {firstname : this.form.firstname, lastname : this.form.lastname, email: this.form.email, password: this.form.password}).then(
					(response) => {
						// after registration, redirect to login if successful
						this.$router.push({name: 'Login', params : {message : response.data.message}})
					},
				)},
			onSubmit(evt){
				evt.preventDefault();
				this.is_success = true
				this.message = ''
				this.register()
			}
		}
	}	
</script>
