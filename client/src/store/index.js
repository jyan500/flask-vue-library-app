import Vue from 'vue'
import Vuex from 'vuex'

// import AJAX functions
import { authenticate, register, logout, libraries, books, genres, search  } from '@/api'
import { isValidJwt, EventBus } from '@/utils'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		user : localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : {},
		jwt: localStorage.getItem('jwt') ? JSON.parse(localStorage.getItem('jwt')) : '',
		cart : localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : []

	},
	getters : {
		isAuthenticated(state){
			return isValidJwt(state.jwt.token)
		},
		getCart(state){
			return state.cart
		}
	},
	mutations: {
		setUserData(state, payload){
			state.user = payload.userData
		},
		resetUserData(state){
			state.user = {};
		},
		resetJwtToken(state){
			state.jwt = '';
			localStorage.removeItem('jwt')
		},
		setJwtToken(state, payload){
			localStorage.setItem('jwt', JSON.stringify(payload.jwt))
			state.jwt = payload.jwt
		},
		addToCart(state, payload){
			state.cart.push(payload.book)	
			localStorage.setItem('cart', JSON.stringify(state.cart))
		}
	},
	actions: {
		addToCart(context, book){
			console.log('book: ', book)
			context.commit('addToCart', {book})
		},
		login(context, userData){
			context.commit('setUserData', { userData })	
			return authenticate(userData)
				.then(
					(response) => {
						context.commit('setJwtToken', { jwt: response.data })
						return response
					}
				)
				.catch(error => {
					console.log('Error Authenticating: ', error)
					EventBus.$emit('failedAuthentication', error.response.data.message)
				})
		},
		register(context, userData){
			context.commit('setUserData', { userData })
			return register(userData)
				.then(
					(response) => {
						return response
					}
				)
				.catch(error => {
					console.log('Error Registering: ', error.response.data.message)	
					EventBus.$emit('failedRegistering', error.response.data.message)
				})
		},
		logout(context){
			context.commit('resetUserData');
			context.commit('resetJwtToken');
			return logout().then(
				(response) => {
					return response
				}
			)
		},
		libraries(){
			return libraries().then(
				(response) => {
					return response
				}
			)
		},
		books(){
			return books().then(
				(response) => {
					return response
				}
			)
		},
		genres(){
			return genres().then(
				(response) => {
					return response
				}
			)
		},
		search(context, searchParams){
			console.log('searchParams: ', searchParams);
			return search(searchParams).then(
				(response) => {
					return response	
				}
			)
		}
	},
	modules: {

	}
})
