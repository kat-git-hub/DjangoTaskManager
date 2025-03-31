# Task Manager

Task manager is a simple web app application developed using the Django framework

FEATURES:

1. User registration and authentication.
2. Task creation and deletion: Users can create new tasks, providing details such as title, description, and other relevant information. They can also delete tasks that have been completed or are no longer needed.
3. Task filtering: The system enables users to filter tasks based on various parameters, such as status.
4. Label creation and deletion: Users can create labels to organize their tasks into categories or types. They can also remove labels when they are no longer required.
5. Status creation and deletion: Users can create statuses for tasks to track their progress or current state. Users also have the ability to delete statuses if they are no longer relevant.



## Tests and linter status

[![Maintainability](https://api.codeclimate.com/v1/badges/dc8ddc3289858828b1f7/maintainability)](https://codeclimate.com/github/kat-git-hub/python-web-development-project-lvl4/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/dc8ddc3289858828b1f7/test_coverage)](https://codeclimate.com/github/kat-git-hub/python-web-development-project-lvl4/test_coverage)  [![linter-check](https://github.com/kat-git-hub/python-web-development-project-lvl4/actions/workflows/linter-check.yml/badge.svg)](https://github.com/kat-git-hub/python-web-development-project-lvl4/actions/workflows/linter-check.yml) 



## What You Will Need

- Python 3.8+ (Python3 and above)

- Django and other dependencies declared in the `pyproject.toml` file

- [Poetry](https://python-poetry.org/docs/#installation)



## Quick Start Guide

Local installation:

1. Clone the project: `$ git clone git@github.com:kat-git-hub/DjangoTaskManager.git`

2. Navigate to the cloned directory: `$ cd DjangoTaskManager`

3. Create a virtual environment using Poetry: `$ poetry install`

4. To activate the virtual environment, use the following command: `$ poetry shell`

5. Install dependencies

6. Open the `.env` file in root directory and add the following line: `SECRET_KEY=your_secret_key_value`

7. Create the database: `$ poetry run python manage.py migrate`
You should run first the `makemigrations` task if changes in the models were made.

8. To run the local server: `$ poetry run python manage.py runserver`

9. Access the application: `http://localhost:8000/`

### Docker

To run the project using Docker, you can follow these steps:

1. Make sure you have [Docker](https://www.docker.com/get-started) installed on your system.

2. Clone the project: `$ git clone git@github.com:kat-git-hub/DjangoTaskManager.git`

3. Navigate to the cloned directory: `$ cd DjangoTaskManager`

4. Build the Docker image: `$ docker-compose build`

5. Run the Docker container: `$ docker-compose up`

6. Access the application in your browser: `http://localhost:8000/`



### Have fun! :tada:
