# Daily Expenses Sharing Application

## Setup
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up a MySQL/PostgreSQL database and update the `SQLALCHEMY_DATABASE_URL` in `database.py`.
4. Run the application using `uvicorn app.main:app --reload`.

## Endpoints
- `/users/` - Create a user.
- `/users/{user_id}/expenses/` - Add an expense.

## Features
- User creation, expense management, expense splitting (equal, exact, percentage).
- Downloadable balance sheet.