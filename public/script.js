const API_URL = "https://books-database.onrender.com";

async function fetchBooks() {
    const response = await fetch(API_URL);
    const books = await response.json();
    const booksList = document.getElementById("books-list");
    booksList.innerHTML = "";

    books.forEach(book => {
        const bookElement = document.createElement("div");
        bookElement.innerHTML = `
            <h2>${book.title}</h2>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Genre:</strong> ${book.genre}</p>
            <p><strong>Year:</strong> ${book.year}</p>
            <p><strong>Description:</strong> ${book.description}</p>
            <button onclick="deleteBook(${book.id})">Delete</button>
            <a href="/static/update-book.html?id=${book.id}">Edit</a>
        `;
        booksList.appendChild(bookElement);
    });
}

async function deleteBook(id) {
    await fetch(`${API_URL}${id}`, { method: "DELETE" });
    fetchBooks();
}

async function addBook(event) {
    event.preventDefault();

    const book = {
        title: document.getElementById("title").value,
        author: document.getElementById("author").value,
        genre: document.getElementById("genre").value,
        year: parseInt(document.getElementById("year").value),
        description: document.getElementById("description").value,
    };

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
    });

    window.location.href = "/static/index.html"; 
}

async function updateBook(event) {
    event.preventDefault();

    const book = {
        title: document.getElementById("title").value,
        author: document.getElementById("author").value,
        genre: document.getElementById("genre").value,
        year: parseInt(document.getElementById("year").value),
        description: document.getElementById("description").value,
    };

    const bookId = document.getElementById("book-id").value;

    await fetch(`${API_URL}${bookId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(book),
    });

    window.location.href = "/static/index.html";
}

if (document.getElementById("books-list")) fetchBooks();

const addBookForm = document.getElementById("add-book-form");
if (addBookForm) addBookForm.addEventListener("submit", addBook);

const updateBookForm = document.getElementById("update-book-form");
if (updateBookForm) {
    const params = new URLSearchParams(window.location.search);
    const bookId = params.get("id");
    if (bookId) {
        document.getElementById("book-id").value = bookId;
    }

    updateBookForm.addEventListener("submit", updateBook);
}
