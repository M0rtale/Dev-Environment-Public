# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents (including app.py) into the container
COPY . .

# Create the blocks directory inside the container
RUN mkdir -p ./blocks

# Run the app.py script when the container launches
CMD ["python", "./app.py"]

