<template>
	<div>
		<b-alert variant = "success" show dismissible>{{ message }}</b-alert>
		<br>
	</div>
</template>
<style>
	
</style>
<script>
	export default {
		props : {
			message : String
		},
		data(){
			return {

			}
		},
		methods : {

		}
	}
</script>