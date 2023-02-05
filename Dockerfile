# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Specify the command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--debugger"]
