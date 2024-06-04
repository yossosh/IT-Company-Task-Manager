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

# 1.Prerequisites
Make sure you have the following installed on your machine:

Python 3.x
Django 3.x or newer
Virtualenv (optional, but recommended)

To get started with our Task Manager, create your own fork and run code like this:

    git clone https://github.com/your-username/IT-Company-Task-Manager.git
    cd IT-Company-Task-Manager




# 2.Installation

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




## Models Structure

![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/0df65b64-1af5-47de-ae63-4a470a104739)




## Screenshots
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/055032b2-8861-4232-b623-59df823a010c)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/dee2e3f6-699b-45c6-abd5-cc539afdaea0)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/d3b2ad38-25e0-48dd-8504-3ef3211791be)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/73b21558-3da7-4ce5-b58c-ad6be170f571)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/2017fe04-e91e-4508-9251-7d2869f15c7d)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/40a056f9-9b07-4ffe-8c78-753b965b01a2)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/48ef7e5e-5758-4e4e-b0d9-53c62303061c)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/4f187fb7-1a3a-4285-99cf-accb8a8f3c2f)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/3c6566d1-85a1-4e81-bf93-a2abf8a3151c)
![image](https://github.com/yossosh/IT-Company-Task-Manager/assets/160421955/1018ca35-f1e8-4dba-ada0-d559a76543a7)



