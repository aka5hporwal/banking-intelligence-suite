FROM python:3.10-slim

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN pip install --no-cache-dir typing-extensions==4.14.1

CMD ["python3", "app.py"]