FROM python:3.11.0b4-bullseye

RUN apt update -y

WORKDIR /backend

COPY . .

RUN pip3 install -r requirements.txt

# expose the ports
EXPOSE 8000

# Command to run Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
