# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies
RUN pip install --upgrade pip && pip install .

# Run the tests
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
