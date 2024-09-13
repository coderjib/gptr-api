FROM python:3.10-slim

WORKDIR /app

# Install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install dumb-init
RUN apt-get update && apt-get install -y dumb-init

# Copy application files
COPY app.py .
COPY .env .

# Install python-dotenv
RUN pip install python-dotenv

# Use dumb-init as the entrypoint
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# Run the application
CMD ["python", "app.py"]