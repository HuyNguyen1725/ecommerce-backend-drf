# Backend API - Django REST Framework
RESTful API built with Django REST Framework, featuring JWT authentication, role-based access control (RBAC), 
and PostgreSQL.

## Tech Stack
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- RBAC (Role-Based Access Control)
- django-cors-headers

## Setup
### Clone Repository
```
git clone https://github.com/HuyNguyen1725/ecommerce-backend-drf
cd ecommerce-backend-drf
```

### Create virtual environment
```
python -m venv venv
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Create .env
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

JWT_SECRET_KEY=your-jwt-secret
```
### Make migrations
```
python manage.py makemigrations
```
### Migrate
```
python manage.py migrate
```
### Run server
```
python manage.py runserver
```
## Frontend Repo
https://github.com/HuyNguyen1725/ecommerce-frontend-react

## Api URL
https://api.huynguyen1725.com

## App URL
https://huynguyen1725.com
