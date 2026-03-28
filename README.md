# BlogSpace

BlogSpace is a simple blog website built with Django.  
It allows users to register, log in, create blog posts, edit or delete their own posts, like posts, and comment on posts.

---

## Features

- User registration and login
- Secure logout
- Create blog posts
- Edit and delete own blog posts
- View all blog posts
- Blog details page
- Comment system
- Like and unlike feature
- View count for each blog
- User profile page showing own blogs
- Django admin panel support
- Rich text blog content using CKEditor5

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- CKEditor5

---

## Project Structure

- `homepage.html` — Homepage
- `posts.html` — Shows all blog posts
- `blog_details.html` — Shows full blog details, likes, comments, and views
- `profile.html` — Shows logged-in user’s own blog posts
- `login.html` — Login page
- `register.html` — Registration page
- `create_edit.html` — Create and edit blog post page

---

## Main Functionalities

### Authentication
Users can:
- Register
- Log in
- Log out

### Blog Management
Authenticated users can:
- Create blog posts
- Edit their own posts
- Delete their own posts

### Blog Details
Users can:
- View full blog content
- Like or unlike a post
- See total likes
- See total views
- Read comments
- Add comments if logged in

### Profile
Users can:
- See their own posts
- Edit or delete their own posts
- Open blog details from profile

---

## Installation

### 1. Clone the project

```bash
git clone https://github.com/rohan9932/blogspace.git
cd blogspace
```

### 2. Create virtual environment
```bash
python -m venv .venv
```
### 3. Activate virtual environment
On windows, 
```bash
.venv\Scripts\activate
```
On MacOs/Linux, 
```bash
source .venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

---

### Admin Panel

You can access the admin panel at:
```bash
http://127.0.0.1:8000/admin/
```
From there, admin can manage:
- Users
-	Blog posts
-	Comments

---

Notes
-	CKEditor5 is used for rich text blog writing.
-	Only logged-in users can create, edit, delete, like, and comment.
-	Users can only edit or delete their own posts.
-	Delete requests are handled using POST for safety.
