# use latest Python image from Docker Hub
FROM python:latest

# set working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY message.txt .
COPY unscramble.py .

# Run the script when the container launches
CMD ["python3", "unscramble.py"]
