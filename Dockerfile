# Use official Python image
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies for graphviz and MySQL
RUN apt-get update && \
    apt-get install -y graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose optional port (if needed for future web/Streamlit version)
EXPOSE 8080

# Default command when container runs
CMD ["python", "main.py"]

