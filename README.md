# Todo-App with Django and Docker

This project is a simple **Todo Application** built with **Django** and containerized using **Docker**. It allows users to create, manage, and mark tasks as completed. The app is designed to run in a Docker container, providing an easy and reproducible environment for development and deployment.

## Features

- User authentication (login and registration).
- Add, edit, delete, and mark tasks as completed.
- Due date functionality for tasks.
- Fully containerized using Docker.

## Tech Stack

- **Backend**: Django
- **Database**: SQLite (for simplicity in development, can be switched to PostgreSQL or another DB in production)
- **Containerization**: Docker

## Prerequisites

- Docker
- Docker Compose
- Python 3.x (for local development without Docker, if necessary)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmirhosseinAmirzadeh/to-do-app.git
cd todo-app
```

### 2. Build and Run with Docker

If you don't have Docker installed, follow the official guide [here](https://docs.docker.com/get-docker/) to install it.

Run the following commands to build and start the app inside a Docker container.

#### Build Docker Images

```bash
docker-compose build
```

#### Start the Application

```bash
docker-compose up
```

This will start the Django app and all necessary services (e.g., database).

### 3. Access the App

Once Docker is up and running, you can access the application in your browser at:

```
http://127.0.0.1:8000
```

### 4. Create Superuser (Optional)

To access the Django admin interface or create an admin user for the app, run the following command in your Docker container:

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to create the superuser account.

## Development

For local development without Docker:

### 1. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Run the Application Locally

```bash
python manage.py runserver
```

### 5. Access the App

Go to `http://127.0.0.1:8000` in your browser.

## Usage

### User Authentication

- Users can sign up, log in, and manage their tasks.
- Each user has their own task list.

### Task Management

- Users can:
  - Add new tasks.
  - Mark tasks as completed.
  - Edit tasks.
  - Delete tasks.
  - View due times for tasks.

## Docker Commands

- To stop the app: `docker-compose down`
- To rebuild the containers: `docker-compose build --no-cache`
- To view logs: `docker-compose logs -f`
- To run migrations in the container: `docker-compose exec web python manage.py migrate`

## Folder Structure

```
TO-DO-APP/
│── core/                  # Main application folder
├── accounts/              # User authentication and management
├── core/                  # Core settings and configurations
│── statics/               # Static files (CSS, JS, images)
├── templates/             # HTML templates for rendering views
├── todo/                  # To-Do application logic
│── db.sqlite3             # SQLite database file
│── manage.py              # Django management script
│── .gitattributes         # Git configuration for repository attributes
│── .gitignore             # Git ignored files
│── docker-compose.yml     # Docker Compose configuration file
│── dockerfile             # Dockerfile for containerization
│── LICENSE                # License file    
│── README.md              # Project documentation
│── requirements.txt       # Dependencies and requirements
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Thank you for your attention 😊❤
