# Use the official Python image as the base image
FROM python:3.9-slim AS production

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && pip install --upgrade pip \
    && pip install poetry \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create and set the working directory
WORKDIR /app

# Copy only the necessary files
COPY pyproject.toml /app/

# Install dependencies with Poetry
RUN poetry config virtualenvs.create false \
    && poetry lock --no-update \
    && poetry install --no-dev --no-interaction --no-ansi

# Install additional dependencies for production
RUN pip install fastapi uvicorn

# Copy the application code
COPY app/main.py /app/app/main.py

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]