
# Shayan Solutions GET API for Product Management System

This Django project allows you to manage products through a RESTful API and an admin panel.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/Khalidd3v/Shayan-Solutions-Test-APP
   cd myproject
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run migrations:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

6. **Access the admin panel at** `http://localhost:8000/admin` **to add, edit, or delete products.**

## API Endpoints

- **Retrieve all products:** `GET /products/`
- **Retrieve a specific product by ID:** `GET /products/<int:pk>/`

## URLs

- /products/: Retrieves a list of all products.
- /products/<int:pk>/: Retrieves details of a specific product by ID.

---
