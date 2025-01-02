# TechForing Project Management Tool

## Project Setup

### Requirements

- Python 3.x
- pipenv (for managing virtual environment and dependencies)

### Steps to Set Up the Project Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_GITHUB_REPO_LINK.git
   cd techforing_project
   ```

2. **Install pipenv**
   ```bash
   pip install pipenv
   ```

3. **Set Up the Virtual Environment and Install Dependencies**
   ```bash
   pipenv install --dev
   ```

4. **Activate the Virtual Environment**
   ```bash
   pipenv shell
   ```

#### Note: If you haven't created a `Pipfile` and `Pipfile.lock` yet, replace step 3 with the following:
```bash
pipenv install django djangorestframework drf-yasg djangorestframework-simplejwt
```



5. **Set Up the Django Project**
   ```bash
   cd techforing_project
   ```

### Steps to Migrate the Database

1. **Create Migrations**
   ```bash
   python manage.py makemigrations
   ```

2. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

### Commands to Run the Server

1. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

### API Documentation

This project uses Swagger for API documentation.

1. **Access the API Documentation**

   Once the server is running, you can access the API documentation at:
   - Swagger UI: `http://127.0.0.1:8000/swagger/`
   - ReDoc: `http://127.0.0.1:8000/redoc/`

### Testing Endpoints

To test the API endpoints, you can use tools like [Postman](https://www.postman.com/) or [Swagger UI](http://127.0.0.1:8000/swagger/).

**List of API Endpoints:**

- **Users:**
  - Register User: `POST /api/users/register/`
  - Login User: `POST /api/users/login/`
  - Get User Details: `GET /api/users/{id}/`
  - Update User: `PUT/PATCH /api/users/{id}/`
  - Delete User: `DELETE /api/users/{id}/`
  
- **Projects:**
  - List Projects: `GET /api/projects/`
  - Create Project: `POST /api/projects/`
  - Retrieve Project: `GET /api/projects/{id}/`
  - Update Project: `PUT/PATCH /api/projects/{id}/`
  - Delete Project: `DELETE /api/projects/{id}/`
  
- **Tasks:**
  - List Tasks: `GET /api/projects/{project_id}/tasks/`
  - Create Task: `POST /api/projects/{project_id}/tasks/`
  - Retrieve Task: `GET /api/tasks/{id}/`
  - Update Task: `PUT/PATCH /api/tasks/{id}/`
  - Delete Task: `DELETE /api/tasks/{id}/`
  
- **Comments:**
  - List Comments: `GET /api/tasks/{task_id}/comments/`
  - Create Comment: `POST /api/tasks/{task_id}/comments/`
  - Retrieve Comment: `GET /api/comments/{id}/`
  - Update Comment: `PUT/PATCH /api/comments/{id}/`
  - Delete Comment: `DELETE /api/comments/{id}/`
 
- **Super Admin details:**
  - Username: `admin`
  - Email address: `admin@admin.com`
  - Password: `admin`
---
