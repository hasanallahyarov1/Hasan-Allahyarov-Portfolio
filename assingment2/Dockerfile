# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install the en_core_web_sm model
RUN python -m spacy download en_core_web_sm


# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the environment variable for Flask app
ENV FLASK_APP app1.py

# Run the command to start Flask app when the container starts
CMD ["flask", "run", "--host", "0.0.0.0"]






