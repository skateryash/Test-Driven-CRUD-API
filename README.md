# CRUD API with Django Rest Framework (DRF)

This project is a simple CRUD (Create, Read, Update, Delete) API built using Django Rest Framework (DRF). It supports basic operations such as creating, retrieving, updating, and deleting resources, with full integration of Swagger for API documentation and test coverage.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Testing the Application](#testing-the-application)
- [API Documentation with Swagger](#api-documentation-with-swagger)
- [Running the Tests with Coverage](#running-the-tests-with-coverage)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Basic CRUD operations using Django Rest Framework.
- Comprehensive API documentation with Swagger and Redoc.
- Test cases for each API endpoint.
- Test coverage reporting.
  
---

## Project Structure

```
.
├── myapp/                  # Main application folder
│   ├── migrations/         # Database migrations
│   ├── models.py           # Database models
│   ├── serializers.py      # Serializers for API data validation
│   ├── views.py            # API views (with CRUD logic)
│   ├── urls.py             # API URLs routing
│   └── tests.py            # Unit tests for API endpoints
├── crudapi/                # Project-level folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # Project-level URL routing
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## Installation

Follow the steps below to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/skateryash/API-Task.git
cd API-Task
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # For Windows use `.venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Run the following command to create the necessary database tables:

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

If you want to access the Django admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

---

## Running the Application

To start the Django development server, use the following command:

```bash
python manage.py runserver
```

The server will be running at `http://127.0.0.1:8000/`.

---

## API Documentation with Swagger

This project uses **drf-yasg** to provide interactive API documentation with Swagger and Redoc.

- **Swagger UI**: 
  - Go to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to view the interactive Swagger documentation.
  
These endpoints provide a detailed description of all available API routes, request formats, and expected responses.

---

## Testing the Application

The project includes unit tests for all API endpoints. To run the tests, use the following command:

```bash
python manage.py test
```

---

## Running the Tests with Coverage

To check test coverage, ensure you have **coverage** installed:

```bash
pip install coverage
```

Then, run the tests with coverage:

```bash
coverage run --source='.' manage.py test
```

To generate an HTML report:

```bash
coverage html
```

The coverage report will be available in the `htmlcov/` directory.

---
