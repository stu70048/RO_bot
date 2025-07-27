FROM python:3.12.7-slim

# Install system dependencies, including GCC and build-essential tools
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

#RUN pip install --no-cache-dir --upgrade pip

# Set the working directory in the container
WORKDIR /app

# Copy the requirements list directly to the container
COPY requirements.txt ./

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code (optional, replace with actual application files)
COPY . ./

# Set the default command (can be changed based on the application needs)
CMD ["python", "main.py"]