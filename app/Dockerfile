# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi && pip install --no-cache-dir uvicorn

# Run app.py when the container launches
CMD ["python", "app.py"]
