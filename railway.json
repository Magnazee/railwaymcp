# Use Python 3.11 alpine for smaller image size
FROM python:3.11-alpine

# Set working directory
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port that Railway will assign
EXPOSE $PORT

# Run the MCP server
CMD ["python", "main.py"]
