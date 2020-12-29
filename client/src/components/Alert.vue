<template>
	<div>
		<b-alert dismissible fade :variant = "is_success ? 'success' : 'danger'" >{{ message }}</b-alert>
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