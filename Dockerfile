FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN apt-get update && apt-get install git -y && apt-get install curl -y

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["python", "main.py"]
