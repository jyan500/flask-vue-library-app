<template>
	<b-container>
		<b-row>
			<b-col>
				<h1>Books</h1>
				<hr><br><br>
				<alert v-show = "message != ''" :message = "message"></alert>
				<button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add Book</button>
				<br><br>
				<table class="table table-hover">
					<thead>
						<tr>
							<th scope="col">Title</th>
							<th scope="col">Author</th>
							<th scope="col">Read?</th>
							<th></th>
						</tr>
					</thead>
					<tbody>
						<tr :key = "index" v-for = "(book, index) in books">
							<td>{{ book.title }}</td>
							<td>{{ book.author }}</td>
							<td>
								<span>{{ book.read ? 'Yes' : ''}}</span>
							</td>
							<td>
								<div class="btn-group" role="group">
									<button type="button" @click = "editBook(book)" v-b-modal.book-update-modal class="btn btn-warning btn-sm">Update</button>
									<button @click = "onDeleteBook(book)" type="button" class="btn btn-danger btn-sm">Delete</button>
								</div>
							</td>
						</tr>
					</tbody>
				</table>
				<div v-if = "loading" class="d-flex justify-content-center mb-3">
					<b-spinner label="Loading..."></b-spinner>
				</div>
			</b-col>
		</b-row>
		<b-modal
			ref = "addBookModal"
			id = "book-modal"
			title = "Add a new book"
			hide-footer>
			<b-form class = "w-100">
				<b-form-group
					id = "form-title-group"
					label = "Title: "
					label-for = "form-title-input"
				>
					<b-form-input
						id = "form-title-input"
						type = "text"
						v-model = "addBookForm.title"
						required
						placeholder = "Enter title"
					>
					</b-form-input>
				</b-form-group>	
				<b-form-group
					id = "form-author-group"
					label = "Author: "
					label-for = "form-author-input"
				>
					<b-form-input
						id = "form-author-input"
						type = "text"
						v-model = "addBookForm.author"
						required
						placeholder = "Enter author"
					>
					</b-form-input>
				</b-form-group>
				<b-form-group
					id = "form-read-group"
				>
					<b-form-checkbox-group
						v-model = "addBookForm.read"
						id = "form-checks"
					>
						<b-form-checkbox value = "true">Read?</b-form-checkbox>
						
					</b-form-checkbox-group>
				</b-form-group>
				<b-button @click.prevent = "onSubmit" variant = "primary">Submit</b-button>
				<b-button @click.prevent = "onReset" variant = "danger">Reset</b-button>
			</b-form>
		</b-modal>
		<b-modal ref="editBookModal"
			id="book-update-modal"
			title="Update"
			hide-footer>
			<b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
				<b-form-group id="form-title-edit-group"
					label="Title:"
					label-for="form-title-edit-input">
					<b-form-input id="form-title-edit-input"
						type="text"
						v-model="editForm.title"
						required
						placeholder="Enter title">
					</b-form-input>
				</b-form-group>
				<b-form-group id="form-author-edit-group"
					label="Author:"
					label-for="form-author-edit-input">
					<b-form-input id="form-author-edit-input"
						type="text"
						v-model="editForm.author"
						required
						placeholder="Enter author">
					</b-form-input>
				</b-form-group>
					<b-form-group id="form-read-edit-group">
					<b-form-checkbox-group v-model="editForm.read" id="form-checks">
					<b-form-checkbox value="true">Read?</b-form-checkbox>
					</b-form-checkbox-group>
				</b-form-group>
				<b-button-group>
					<b-button type = "submit" variant="primary">Update</b-button>
					<b-button type="reset" variant="danger">Cancel</b-button>
				</b-button-group>
			</b-form>
			</b-modal>
	</b-container>
</template>
<style>
	
</style>
<script>
	import axios from 'axios';
	import Alert from './Alert.vue';
	export default {
		props :{

		},
		components : {
			alert : Alert,
		},
		data(){
			return {
				books : [],
				addBookForm : {
					title : '',	
					author : '',
					read : []
				},
				editForm: {
					id: '',
					title: '',
					author: '',
					read: [],
				},
				message : '',
				loading: false,
			}
		},
		created(){
			this.getBooks()
		},
		methods : {
			editBook(book){
				this.editForm = book;
			},
			getBooks(){
				const path = "http://localhost:5000/books"
				axios.get(path).then(
					(response) => {
						this.books = response.data.books
					}
				).catch(
					(error) => {
						console.log(error)
					}
				)
			},
			addBook(payload){
				this.message = '';
				this.loading = true;
				const path = 'http://localhost:5000/books';	
				axios.post(path, payload).then(
					() => {
						this.getBooks();
						this.loading = false;
						this.message = 'Book added';

					}).catch(
						(error) => {
							console.log(error)	
							this.getBooks()
							this.loading = false;
						}
					)
			},
			updateBook(payload, book_id){
				this.message = '';
				this.loading = true;
				const path = `http://localhost:5000/books/${book_id}`;
				axios.put(path, payload).then(
					() => {
						this.message = 'Book updated!';
						this.getBooks();
						this.loading = false;
					}).catch(
						(error) => {
							console.log(error)	
							this.getBooks();
							this.loading = false;
						}
					);
			},
			removeBook(book_id){
				this.message = '';
				this.loading = true;
				const path = `http://localhost:5000/books/${book_id}`
				axios.delete(path).then(() => {
					this.message = 'Book removed!';
					this.getBooks();
					this.loading = false;
				}).catch((error) => {
					console.log(error);
					this.getBooks();
					this.loading = false;
				});
			},
			initForm(){
				this.addBookForm.title = '';
				this.addBookForm.author = '';
				this.addBookForm.read = [];
				this.editForm.id = "";
				this.editForm.title = "";
				this.editForm.author = "";
				this.editForm.read = [];
			},
			onSubmit(evt){
				this.message = '';
				evt.preventDefault();
				this.$refs.addBookModal.hide();
				let read = false;
				if (this.addBookForm.read[0]) {
					read = true;	
				}
				const payload = {
					title : this.addBookForm.title,
					author : this.addBookForm.author,
					read : read
				}
				this.addBook(payload)
				this.initForm();
			},
			onReset(evt){
				this.message = '';
				evt.preventDefault();
				this.$refs.addBookModal.hide();
				this.initForm();
			},
			onSubmitUpdate(evt){
				evt.preventDefault();
				this.$refs.editBookModal.hide();
				let read = false;
				if (this.editForm.read[0]) {
					read = true;
				}
				const payload = {
					title : this.editForm.title,
					author : this.editForm.author, 
					read, 
				};
				this.updateBook(payload, this.editForm.id);
			},
			onResetUpdate(evt){
				evt.preventDefault();
				this.$refs.editBookModal.hide();
				this.initForm();
				this.getBooks();
			},
			onDeleteBook(book){
				this.removeBook(book.id)
			}
		},
		

	}	
</script>