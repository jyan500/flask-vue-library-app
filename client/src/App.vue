<template>
	<div id="app">
		<Header></Header>
		<b-container class = "mt-5">
			<router-view/>
		</b-container>
	</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
 
i {
	font-size: 1.2em;	
	cursor: pointer;
}
</style>

<script>
	import Header from './components/Header.vue'
	export default {
		components : {
			Header
		}	
	}
</script>