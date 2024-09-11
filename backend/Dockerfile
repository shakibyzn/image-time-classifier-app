FROM python:3.11.10-slim

WORKDIR /backend

# Install git and dependencies needed to build the application
RUN apt-get update && apt-get install -y \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
COPY requirements.txt .

RUN pip3 install -r requirements.txt

RUN pip3 install pytest

COPY . .

# expose the ports
EXPOSE 8000

# Command to run Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]