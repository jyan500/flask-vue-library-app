<template>
	<div>
		<h2>Catalog</h2>	
		<b-form @submit = "onSubmit">
			<b-row>
				<b-col md = "auto">
					<b-form-group label = "Title" label-for = "title">
						<b-form-input id = "title" v-model = "form.title"></b-form-input>	
					</b-form-group>	
				</b-col>	
				<b-col md = "auto">
					<b-form-group label = "Library" label-for = "library_id">
						<b-form-select id = "library_id" v-model = "form.library_id">
							<b-form-select-option value = "0">-- All --</b-form-select-option>	
							<b-form-select-option v-for = "library in libraries" :key = "library.id" :value = "library.id">{{library.name}}</b-form-select-option>
						</b-form-select>
					</b-form-group>
				</b-col>	
				<b-col md = "auto">
					<b-form-group label = "Genre" label-for = "genre_id">
						<b-form-select id = "genre_id" v-model = "form.genre_id">
							<b-form-select-option value = "0">-- All --</b-form-select-option>
							<b-form-select-option v-for = "genre in genres" :key = "genre.id" :value = "genre.id">{{genre.name}}
							</b-form-select-option>
						</b-form-select>	
					</b-form-group>	
				</b-col>	
				<b-col md = "auto">
					<b-form-group>
						<b-button style = "margin-top:30px;" type = "submit" variant = "primary">Search</b-button>	
					</b-form-group>	
				</b-col>	
				<b-col md = "auto">
					
				</b-col>	
				<b-col md = "auto">
					
				</b-col>	
			</b-row>	
		</b-form>
		<div v-if = "!loading">
			<b-table id = "catalog" :fields = "fields" :items = "books" :per-page = "per_page" :current-page = "current_page">
				<template #cell(image_url)="row"><img width = "150" height = "210" :src = "row.value"/></template>
				<template #cell(genre)="row"><span>{{row.value.name}}</span></template>
				<template #cell(actions)="row">
					<b-button size="sm" @click="row.toggleDetails">
					{{ row.detailsShowing ? 'Hide' : 'Show' }} Availability
					</b-button>
				</template>
				<template #row-details="row">
					<b-card>
						<table class = "table">
							<thead>
								<th>Library</th>	
								<th>Status</th>	
							</thead>
							<tbody>
								<tr :key = "key" v-for = "(value, key) in row.item.library">
									<td>{{key}}</td>
									<td>{{value}}</td>
								</tr>	
							</tbody>
						</table>
					</b-card>
				</template>
			</b-table>
		</div>
		<div v-else>
			<b-spinner></b-spinner>	
		</div>
		<b-pagination v-model = 'current_page' :total-rows = "rows" :per-page = "per_page" aria-controls = "catalog">
		</b-pagination>
	</div>
</template>
<style>
	
</style>
<script>
	export default {
		props : {

		},
		data(){
			return {
				per_page : 10,
				current_page : 1,
				libraries : [],
				books : [],
				genres : [],
				loading : false,
				fields : [
					{ key : 'image_url', label : 'Image'},	
					{ key : 'title', label : 'Title', sortable : true},	
					{ key : 'author', label : 'Author', sortable : true},	
					{ key : 'genre', label : 'Genre'},	
					{ key: 'actions', label: '' }
				],
				headers : [
					{

					}
				],
				form : {
					title : '',
					library_id : 0,
					genre_id : 0,
				}

			}
		},
		mounted(){
			this.getLibraries();
			this.getBooks();
			this.getGenres();
		},
		computed : {
			rows(){
				return this.books.length
			}
		},
		methods : {
			getLibraries(){
				this.$store.dispatch('libraries').then(
					(response) => {
						this.libraries = response.data.data
					}
				)
			},
			getBooks(){
				this.$store.dispatch('books').then(
					(response) => {
						this.books = response.data.data
					}
				)
			},
			getGenres(){
				this.$store.dispatch('genres').then(
					(response) => {
						this.genres = response.data.data
					}
				)
			},
			onSubmit(e){
				e.preventDefault()
				let url_params = [];
				let search_url = '?';
				for (let key in this.form){
					url_params.push(key + '=' + this.form[key])
				}
				console.log(url_params.join('&'))
				search_url = search_url + url_params.join('&');
				this.$store.dispatch('search', search_url).then(
					(response) => {
						this.books = response.data.data
					},
					(error) => {
						console.log(error)
					}

				)

			}

		}
	}	
</script>