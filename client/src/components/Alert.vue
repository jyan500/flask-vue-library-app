<template>
	<div>
		<b-alert :variant = "is_success ? 'success' : 'danger'" show>{{ message }}</b-alert>
		<br>
	</div>
</template>
<style>
	
</style>
<script>
	export default {
		props : {
			message : String,
			is_success : {
				type : Boolean,
				default : true 
			} 
		},
		data(){
			return {
			}
		},
		methods : {

		}
	}
</script>