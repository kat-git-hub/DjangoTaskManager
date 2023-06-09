### Task Manager

Task manager is a simple web app application developed using the Django framework

FEATURES:

1. User registration and authentication.
2. Task creation and deletion: Users can create new tasks, providing details such as title, description, and other relevant information. They can also delete tasks that have been completed or are no longer needed.
3. Task filtering: The system enables users to filter tasks based on various parameters, such as status.
4. Label creation and deletion: Users can create labels to organize their tasks into categories or types. They can also remove labels when they are no longer required.
5. Status creation and deletion: Users can create statuses for tasks to track their progress or current state. Users also have the ability to delete statuses if they are no longer relevant.

----

### Tests and linter status:
[![Actions Status](https://github.com/kat-git-hub/python-web-development-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/kat-git-hub/python-web-development-project-lvl4/actions)  [![Maintainability](https://api.codeclimate.com/v1/badges/dc8ddc3289858828b1f7/maintainability)](https://codeclimate.com/github/kat-git-hub/python-web-development-project-lvl4/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/dc8ddc3289858828b1f7/test_coverage)](https://codeclimate.com/github/kat-git-hub/python-web-development-project-lvl4/test_coverage)  [![linter-check](https://github.com/kat-git-hub/python-web-development-project-lvl4/actions/workflows/linter-check.yml/badge.svg)](https://github.com/kat-git-hub/python-web-development-project-lvl4/actions/workflows/linter-check.yml)

----

### **Quick Start Guide**

What You Will Need

Python 3.8+ (Python3 and above)
Django and other dependencies declared in the requirements.txt file
[Poetry](https://python-poetry.org/docs/#installation)



Clone the project: `$ git clone git@github.com:kat-git-hub/DjangoTaskManager.git`
Navigate to the cloned directory: `$ cd DjangoTaskManager`
Create a virtual environment using Poetry: `$ poetry install`
To activate the virtual environment, use the following command: `$ poetry shell`
Install dependencies with: `$ pip install -r requirements.txt`
Open the `.env` file in root directory and add the following line: `SECRET_KEY=your_secret_key_value`
Create the database: `$ poetry run python manage.py migrate`
You should run first the `makemigrations` task if changes in the models were made.
To run the local server: `$ poetry run python manage.py runserver`
Access the application: `http://localhost:8000/`

Have fun!