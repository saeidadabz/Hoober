Features

User authentication (signup/login).

Role-based access control (Admin, User, Consultant, Employer).

CRUD operations for job postings.

Job application submission and status update.

Consultation session booking and reservation.

Tech Stack

Backend: Django, Django REST Framework

Database: PostgreSQL (or SQLite, if preferred)

Authentication: JWT (JSON Web Token)

Other Tools: Docker (optional), Swagger for API documentation

Requirements

Python 3.8 or higher

Django 3.x or higher

Django REST Framework

PostgreSQL (or any other database you are using)

Setup and Installation

Clone the repository:

git clone (https://github.com/saeidadabz/Hoober.git)

Install dependencies:
pip install -r requirements.txt

Create and apply migrations:
python manage.py migrate

Create a superuser (optional):
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the API documentation at:
http://127.0.0.1:8000/swagger/
