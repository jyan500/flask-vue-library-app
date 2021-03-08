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

export function libraries(){
	return axios.get(`${API_URL}/libraries`)
}

export function books(){
	return axios.get(`${API_URL}/books`)
}

export function genres(){
	return axios.get(`${API_URL}/genres`)
}

export function search(searchParams){
	return axios.get(`${API_URL}/search${searchParams}`)	
}

export function checkout(data, jwt){
	return axios.post(`${API_URL}/checkout`, data, { headers : {Authorization : `Bearer: ${jwt}`} })
}

export function user_books(jwt){
	return axios.get(`${API_URL}/user-books`, { headers : {Authorization : `Bearer: ${jwt}`}})
}