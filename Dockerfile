# Stage 1: Build the wheel file
FROM python:3.9-slim as builder

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install build dependencies
RUN pip install --upgrade pip setuptools wheel

# Build the wheel file
RUN python setup.py bdist_wheel

# Stage 2: Create the final image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the wheel file from the builder stage
COPY --from=builder /app/dist/*.whl /app/

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install the wheel file
RUN pip install /app/*.whl

# Run the tests to verify installation
COPY tests/ /app/tests/
CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
