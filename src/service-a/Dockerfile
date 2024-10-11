# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and the Python script into the container
COPY requirements.txt .
COPY bitcoin_fetcher.py .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "bitcoin_fetcher.py"]
