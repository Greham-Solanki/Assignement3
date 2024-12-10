# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app files to the container
COPY . /app

# Install dependencies
RUN pip install Flask

# Expose port 80
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
