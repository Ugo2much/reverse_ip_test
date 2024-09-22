# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any required dependencies
RUN pip install --no-cache-dir Flask

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable to prevent Python from buffering output (for logs)
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"]
