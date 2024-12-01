FROM python:3.9-slim

# Install system dependencies required for OpenCV and Flask
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container (including model files)
COPY . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to indicate the app should run in the container
ENV FLASK_APP=mobdetapp.py

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
