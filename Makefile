install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 task_manager
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml
migrate:
	poetry run python manage.py migrate
migrations:
	poetry run python manage.py makemigrations
runserver:
	poetry run python manage.py runserver