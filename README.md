# Jumpcloud-demo
Thank you for the opportunity and challenge with this exercise. I thought it was important to provide the solution for this problem while demonstrating my ability to create a development and release pipeline workflow. I've never actually used Github Actions before, so this was all a valuable learning experience. In this repo you'll find my solution in the **service.py** file and some unit tests in the **test-service.py** file. I used Postman to mock the API backend server. In the "Actions" tab you can view my pipeline activity. Currently, code pushed to any branch is built, linted and tested. For branches labeled **release-** the code is built, linted, tested and then pushed to my Dockerhub registry. There are  instructions below for building and running the project locally as well as using Docker.

## Pull image from Dockerhub
```
docker pull bsumn3r/jumpcloud-registry:latest
```
Run the image:
```
docker run bsumn3r/jumpcloud-registry:latest
```

## Build using Docker
To build the application using Docker run the following commands from the root directory:
```
docker build -f Dockerfile -t <tag-name>
```

## Dependencies
For building locally, you will need Python 3.x or higher. You can download Python 3 here:
```
https://www.python.org/downloads/
```
From the root directory, you'll then need to run the following commands:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install flake8 pytest
```
To run the application, from the root directory, use the command:
```
python service.py
```
