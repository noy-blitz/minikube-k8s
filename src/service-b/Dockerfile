# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8081

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file (if you have one) and the application code
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8081

# Command to run the Flask app
CMD ["flask", "run"]
