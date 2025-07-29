## Parent Image
FROM python:3.12-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


## Copying all contents from local to app
COPY . .

## Run setup.py to install the package
## ignore cache to reduce image size
RUN pip install --no-cache-dir -e .     


# Used PORTS
EXPOSE 8501

## Command to run the application
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]
