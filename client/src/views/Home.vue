<template>
	<b-container>
		<b-row>
			<alert v-show = "message != ''" :message = "message"></alert>
		</b-row>
		<b-row>
			<h2>Home</h2>	
		</b-row>

	</b-container>
</template>
<style>
</style>
<script>
	import Alert from '../components/Alert.vue';
	export default {
		components : {
			'alert' : Alert
		},
		props : {

		},
		data(){
			return {
				message : this.$route.params.message ? this.$route.params.message : ''
			}	
		}
	}	
</script>