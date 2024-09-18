# BookNest

BookNest is a digital library designed to let users explore and borrow books effortlessly. With smart filters, it makes browsing through a wide range of categories—from fiction to technology—a breeze. On the admin side, managing the library is just as simple, with tools to easily add new titles, track borrowed books, and monitor availability.

# PROJECT DESCRIPTION

You have been tasked to develop an application to manage books in a library. With your application, users can browse through the catalogue of books and borrow them. You are to build 2 independent API services for this application.

1. Frontend API

This API will be used to

- Enroll users into the library using their email, firstname and lastname.
- List all available books
- Get a single book by its ID
- Filter books
  - by publishers e.g Wiley, Apress, Manning
  - by category e.g fiction, technology, science
- Borrow books by id (specify how long you want it for in days)

2. Backend/Admin API

This API will be used by an admin to:

- Add new books to the catalogue
- Remove a book from the catalogue.
- Fetch / List users enrolled in the library.
- Fetch/List users and the books they have borrowed
- Fetch/List the books that are not available for borrowing (showing the day it will be available)
