# Django Blog Platform

A simple blog web application built with Django.

## Features

- User registration and login
- Create, read, update, delete blog posts
- Image upload support for posts
- Login required to create/edit/delete posts

## Tech Stack

- Python
- Django
- SQLite
- HTML/CSS

## Setup

1. Clone the repository
   
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo

2. Create a virtual environment
   
   python -m venv .venv
   .venv\Scripts\activate

3. Install dependencies
   
   pip install django pillow

4. Run migrations
   
   python manage.py migrate

5. Create a superuser (optional, for admin panel)
   
   python manage.py createsuperuser

6. Run the server
   
   python manage.py runserver

7. Open http://127.0.0.1:8000

## Pages

- `/` - Home, list of all posts
- `/login` - Login
- `/register` - Register
- `/create` - Create a new post
- `/post/<id>` - View a post
- `/update/<id>` - Edit a post
- `/delete/<id>` - Delete a post
- `/logout` - Logout