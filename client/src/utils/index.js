// event bus to send messages around the application, such as failure to authenticate via JWT
import Vue from 'vue'

export const EventBus = new Vue()
export const API_URL = 'http://localhost:5000'

// determine whether jwt is valid
export function isValidJwt(jwt){
	if (!jwt || jwt.split('.').length < 3){
		return false
	}

	// token = [HEADER].[PAYLOAD].[SIGNATURE]
	const token_parts = jwt.split('.')
	const data = JSON.parse(atob(token_parts[1]))
	const exp = new Date(data.exp * 1000) // JS deals with dates in milliseconds since epoch
	const now = new Date()
	// if instantiation time of the JWT has not passed the expiration date, it is still valid 
	return now < exp

}

