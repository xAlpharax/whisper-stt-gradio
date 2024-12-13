# Use an official CUDA base image with pytorch
FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

# Install python3 and pip3
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv git ffmpeg

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment in future commands
ENV PATH="/app/venv/bin:$PATH"

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py ./

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application
CMD ["python", "app.py"]
