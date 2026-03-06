# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Set environment variables to ensure Python output is logged correctly
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install system dependencies for PostgreSQL (needed for psycopg2)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy the requirements file into the container
COPY requirements.txt /app/

# 6. Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# 7. Copy the rest of your Django project code into the container
COPY . /app/

# 8. Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]