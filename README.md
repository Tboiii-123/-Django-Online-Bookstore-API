
---


```markdown
# 📚 Online Bookstore API

A simple Django REST Framework project that serves as an online bookstore. Users can view, create, update, and delete books. Authenticated actions require JWT-based login.

---

## 🚀 Features

- JWT Authentication (Register/Login)
- Full CRUD for Books
- API built with Django REST Framework
- Interactive Swagger Docs
- Plain HTML/CSS/JS Frontend for book management

---

## 📁 Project Structure

```

bookstore/            # Django project
├── books/            # App with models, views, urls
└── templates/        # Optional templates if added

frontend/             # Plain HTML/CSS/JS frontend
├── index.html
├── style.css
└── script.js

requirements.txt
README.md

````

---

## ⚙️ Setup Instructions

### 🐍 Backend (Django)

1. **Clone the repo**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
````

2. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. **Visit Swagger API Docs**

```
http://127.0.0.1:8000/swagger/
```

````

---


```markdown
---



## 🔐 API Endpoints

| Method | Endpoint                | Description                      | Auth |
|--------|-------------------------|----------------------------------|------|
| POST   | `/api/register/`        | Register new user                | ❌   |
| POST   | `/api/login/`           | Login and get JWT token          | ❌   |
| GET    | `/api/books/`           | List all books                   | ❌   |
| GET    | `/api/books/{id}/`      | Retrieve book details            | ❌   |
| POST   | `/api/books/`           | Create new book                  | ✅   |
| PUT    | `/api/books/{id}/`      | Update book                      | ✅   |
| DELETE | `/api/books/{id}/`      | Delete book                      | ✅   |
| POST   | `/api/token/refresh/`   | Refresh expired JWT token        | ✅   |

---


## 📝 Tech Stack

* Django 4.x
* Django REST Framework
* JWT Auth (`djangorestframework-simplejwt`)
* Swagger (`drf-yasg`)

````

---


```markdown
---

## 🧠 TODO / Extras (Optional)

- ✅ Add `PUT` support on frontend
- ✅ Token auto-refresh
- 🚀 Deploy to Heroku / Render
- 🎨 Improve UI with Bootstrap or TailwindCSS

---

## 🤝 Author

**Lawal Hussein Taiwo**  
Python & Django Developer  
[Portfolio](#) | [GitHub](https://github.com/Tboiii-123)

---

## 📄 License

This project is licensed under the MIT License.
````

---

Let me know if you'd like:

* A ZIP file of the entire frontend
* Custom README preview with badges
* A walkthrough video script or YouTube demo

I'm here to help you impress the recruiter ✅
