import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Books from '../components/Books.vue'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import store from '../store/index.js'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

const routes = [
	{
		path : '/',
		name : 'Home',
		component : Home
	},
	{
		path: '/login',
		name: 'Login',
		component : Login
	},
	{
		path: '/register',
		name : 'Register',
		component : Register,
	},
	{
		path : '/books',
		name : 'Books',
		component : Books,
		beforeEnter(to, from, next){
			if (!store.getters.isAuthenticated){
				next('/login')
			}	
			else {
				next()
			}
		}
	},
]

const router = new VueRouter({
 mode: 'history',
  base: process.env.BASE_URL,
  routes : routes
})

export default router
