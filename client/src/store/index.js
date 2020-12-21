import Vue from 'vue'
import Vuex from 'vuex'

// import AJAX functions
import { authenticate, register, logout } from '@/api'
import { isValidJwt, EventBus } from '@/utils'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		user : {},
		jwt: ''

	},
	getters : {
		isAuthenticated(state){
			return isValidJwt(state.jwt.token)
		}
	},
	mutations: {
		setUserData(state, payload){
			console.log('setUserData payload = ', payload)
			state.user = payload.userData
		},
		resetUserData(state){
			state.user = {};
		},
		resetJwtToken(state){
			state.jwt = '';
		},
		setJwtToken(state, payload){
			console.log('setJwtToken payload = ', payload)
			localStorage.token = payload.jwt.token
			state.jwt = payload.jwt
		}
	},
	actions: {
		login(context, userData){
			context.commit('setUserData', { userData })	
			return authenticate(userData)
				.then(response => context.commit('setJwtToken', { jwt: response.data }))
				.catch(error => {
					console.log('Error Authenticating: ', error)
					EventBus.$emit('failedAuthentication', error)
				})
		},
		register(context, userData){
			context.commit('setUserData', { userData })
			return register(userData)
				.then(
				)
				.catch(error => {
					console.log('Error Registering: ', error.response.data.message)	
					EventBus.$emit('failedRegistering', error.response.data.message)
				})
		},
		logout(context){
			context.commit('resetUserData');
			context.commit('resetJwtToken');
			return logout()
		},
	},
	modules: {

	}
})
