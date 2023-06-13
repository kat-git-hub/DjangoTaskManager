# Python base image
FROM python:3.9

# Set the environment variable for the container
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the project dependencies
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Run migrations and start the Django server
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
