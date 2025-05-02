# Django Contact Book

A simple web-based Contact Book built with Django. It allows users to register, log in, and manage their personal contact list with CRUD operations and search functionality.

## 🚀 Features

- User Registration & Login (Django’s default auth system)
- Add, Update, Delete, and View Contacts
- Search contacts by name, phone, email, or address
- Secure: Each user can only access their own contacts

## 🛠️ Setup Instructions

### 1. Clone the project

```bash
git clone https://github.com/your-username/contactbook.git
cd contactbook
```
### 2. Create and activate a virtual environment

python -m venv cb
# On Windows:
cb\Scripts\activate
# On Mac/Linux:
source cb/bin/activate

pip install django

python manage.py migrate

python manage.py runserver

##👤 Login Info
You can log in using the superuser credentials created above, or register a new user through the UI.

