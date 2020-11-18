import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import Ping from '../components/Ping.vue'
import Books from '../components/Books.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

const routes = [
	{
		path : '/',
		name : 'Books',
		component : Books
	},
	{
		path : '/ping',
		name : 'Ping',
		component: Ping	
	},
]

const router = new VueRouter({
 mode: 'history',
  base: process.env.BASE_URL,
  routes : routes
})

export default router
