# Dockerfile

# Pull the official python image
# Indicates the base image on which the application will be built inside the container.
FROM python:3.9

# Set a working directory
WORKDIR /app

# Copy dependencies of the project in workdir
COPY ./requirements.txt /app/requirements.txt

# Install dependencies in the workidir of the container
RUN pip install -r /app/requirements.txt

# Define the command with which our application will be executed inside the container
CMD python manage.py runserver 0.0.0.0:8000
