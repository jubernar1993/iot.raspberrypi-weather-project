FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY . /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    && apt-get clean

# Install Python dependencies
RUN pip install --upgrade pip

# Install the AWS IoT SDK
RUN pip install AWSIoTPythonSDK

# Command to create the Python virtual environment and activate it
RUN python3 -m venv venv
RUN . /app/venv/bin/activate
# Expose necessary ports, if any
EXPOSE 8080

# Set the default command for the container (e.g., run your Python script)
CMD ["/app/venv/bin/python", "publish_message.py"]
