import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Catalog from '../views/Catalog.vue'
import CartView from '../views/CartView.vue'
import Checkout from '../views/Checkout.vue'
import Books from '../views/Books.vue'
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
		path : '/catalog',
		name : 'Catalog',
		component : Catalog,
	},
	{
		path : '/cart',
		name : 'CartView',
		component : CartView,
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
	{
		path : '/checkout',
		name : 'Checkout',
		component : Checkout,
		beforeEnter(to, from ,next){
			if (!store.getters.isAuthenticated){
				next('/login')
			}
			else {
				next()
			}
		}		
	}
]


const router = new VueRouter({
 mode: 'history',
  base: process.env.BASE_URL,
  routes : routes
})

export default router
