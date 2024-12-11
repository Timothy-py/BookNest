# BookNest

## Overview
BookNest is a digital library designed to let users explore and borrow books effortlessly. With smart filters, it makes browsing through a wide range of categories—from fiction to technology—a breeze. On the admin side, managing the library is just as simple, with tools to easily add new titles, track borrowed books, and monitor availability.

## Project Description
Development of an application to manage books in a library. With this application, users can browse through the catalogue of books and borrow them. Build 2 independent API services for this application.

## Frontend API
This API will be used to:

- Enroll users into the library using their email, firstname and lastname.
- List all available books
- Get a single book by its ID
- Filter books
  - by publishers e.g Wiley, Apress, Manning
  - by category e.g fiction, technology, science
- Borrow books by id (specify how long you want it for in days)

## Backend/Admin API
This API will be used by an admin to:

- Add new books to the catalogue
- Remove a book from the catalogue.
- Fetch / List users enrolled in the library.
- Fetch/List users and the books they have borrowed
- Fetch/List the books that are not available for borrowing (showing the day it will be available)

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.10+
- PostgreSQL
- Docker and Docker Compose (optional, for containerized deployment)

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:Timothy-py/BookNest.git
   cd BookNest
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables in a `.env` file using the .env.example provided:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/library_db
   ```

## Running the Application
1. Start the FastAPI server:
   ```bash
   fastapi dev main.py --reload
   ```

3. Access the API documentation:
   - Frontend Swagger UI: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
   - Admin Swagger UI: [http://127.0.0.1:8081/docs](http://127.0.0.1:8081/docs)

## Running the Application with Docker Compose
1. Ensure you have Docker and Docker Compose installed.

2. Create a `.env` in the root directory of the project using the .env.example file:

3. Start the application with Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. The APIs will be accessible at `http://localhost:8080` and `http://localhost:8081`.

## Database Setup
The database module automatically handles:
- Connection management
- Database creation (if it does not exist)
- Table creation on startup

For managing migrations, consider using **Alembic**:
```bash
pip install alembic
alembic init migrations
```

## Testing
Run the tests using:
```bash
pytest
```
Ensure the test database is configured in your environment variables.

## Contributing
I welcome contributions! Feel free to open issues or submit pull requests.

## Contact me
adeyeyetimothy33@gmail.com
