
Flask Reverse IP Application
=============================

This is a simple Flask web application that returns the reversed IP address of the client making the request. The app is containerized using Docker.

Features
--------
- Displays the client's IP address in reverse order.
- Lightweight and simple Flask application.
- Containerized using Docker for easy deployment.

Prerequisites
-------------
Before you can run this project, ensure you have the following installed:
- Docker (for building and running the container)

Getting Started
---------------
1. Clone the Repository:

    git clone <repository-url>
    cd <repository-directory>

2. Build the Docker Image:

    In the project directory where the Dockerfile is located, run the following command to build the Docker image:

    docker build -t flask-app .

    This will create a Docker image with the tag `flask-app`.

3. Run the Docker Container:

    Once the image is built, you can run the container with the following command:

    docker run -p 5000:5000 flask-app

    This will run the Flask app inside the container and expose it on port 5000. You can access it by navigating to http://localhost:5000 (or http://<your-ec2-public-ip>:5000 if running on an EC2 instance).

4. Verify the Application:

    You can verify the app is working by visiting:

    http://localhost:5000

    Or, if on a remote server like EC2:

    http://<your-ec2-instance-ip>:5000

    The app will display the reversed IP address of the client making the request.

Running in Detached Mode
------------------------
To run the container in the background (detached mode), use:

    docker run -d -p 5000:5000 flask-app

Stopping the Container
----------------------
To stop the running container, find the container ID with:

    docker ps

Then stop the container using:

    docker stop <container-id>

Project Structure
-----------------
    .
    ├── app.py             # Flask application code
    ├── Dockerfile         # Dockerfile to build the image
    └── README.md          # Documentation for the project

Technologies Used
-----------------
- Python 3.x
- Flask
- Docker

