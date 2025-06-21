# Bookstore portal

**bookstore_portal** shows and interact with books in the website.

It depends on **bookstore_backend**.

## How it works

- Create books in the backend
- Access the books page in the web portal (e.g. http://localhost:8069/books)

## Technical considerations of the bookstore_portal 

The bookstore_portal shows the books that have been created. 

It has 3 components :

### the Search component

It is a component that adds the search functionnality :
- it fetches the books via the controller **/books/search/**
- it add takes the values entered by the user in the **searchInput** --> **function doSearch()**
- filter the result that comes from the controller when you type ENTER key --> **function doSearch()**
- it renders the result or show a not found result --> **function displayFiltered()**

In the function **doSearch()**, we use **async/await** because we need to wait for the data to be retrieved from the controller before we can use it.

### the List component

It is a component that shows the list of books:
- it fetches the books via a controller **/books/list/data**
- it keeps the result in a state using the **useState** hook that will be used to update the UI
- it interact with the **Search** component to implement the search  functionality

### the App component

It is the entrypoint of our components system and uses the **List** component to show the UI

### Register the components

If the components are not registered, no result we be shown in the UI. This is where **js/main.js** file comes.
When the DOM is ready, the UI elements will be mounted in the app element that has been defined.
