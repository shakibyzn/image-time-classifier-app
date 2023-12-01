FROM python:3.11.0b4-bullseye

RUN apt update -y

WORKDIR /frontend

COPY . .

RUN pip3 install -r requirements.txt

# expose the ports
EXPOSE 8501

# Command to run Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
