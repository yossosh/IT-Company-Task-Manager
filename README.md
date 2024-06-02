# IT Company Task Manager

Welcome to the Task Manager repository!

This project is a comprehensive tool designed to streamline the workflow of a development team, including Developers, Designers, Project Managers, and QA specialists. My Task Manager is created to efficiently handle all aspects of product development, ensuring seamless collaboration and timely completion of tasks.




## Features

Task Creation: Any team member can create a task, providing a detailed description, due date, and priority level.

Task Assignment: Assign tasks to specific team members based on their role and expertise.

Task Completion: Mark tasks as completed once they are done, allowing for clear visibility of accomplished work.

Task Types: All tasks can be divided into types.

User Roles: Differentiate between roles such as Developers, Designers, Project Managers, and QA specialists to assign and manage tasks effectively.

Tags: You can create any tags you need and add them to tasks to search for tasks by tags.

Positions: It is possible to create employees by giving them a position. Also, create your own custom positions.




## Getting Started

# Prerequisites
Make sure you have the following installed on your machine:

Python 3.x
Django 3.x or newer
Virtualenv (optional, but recommended)

To get started with our Task Manager, create your own fork and run code like this:

    git clone https://github.com/your-username/IT-Company-Task-Manager.git
    cd IT-Company-Task-Manager




## Installation

Create and activate a virtual environment:
    
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

    pip install -r requirements.txt

Apply migrations to set up your database:

    python manage.py migrate

Create a superuser (optional, for admin access):

    python manage.py createsuperuser

Run the development server:

    python manage.py runserver




## Running the Tests

To run the tests for the project, use the following command:

    python manage.py test




## Project Structure

The project structure is as follows:

    IT-Company-Task-Manager/
    │
    ├── manager/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │
    ├── static/
    │
    ├── task_manager/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   ├── templates/
    │
    ├── .gitignore
    ├── db.sqlite3
    ├── manage.py
    ├── README.md
