# Use a slim version of Python 3.9 as the base image
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory on the host to the /app directory in the container
COPY . /app

# Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask to run on
EXPOSE 5000

# Set the default command to run when the container starts
# This will run the Flask app inside the container
CMD ["python", "app.py"]
