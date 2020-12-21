import axios from 'axios'
import {API_URL} from '@/utils'

export function authenticate(userData){
	return axios.post(`${API_URL}/login`, userData)
}

export function register(userData){
	return axios.post(`${API_URL}/register`, userData)
}

export function logout(){
	return axios.post(`${API_URL}/logout`)
}