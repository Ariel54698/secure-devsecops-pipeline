FROM python:3.11-slim-bookworm

WORKDIR /app

COPY . .

RUN apt-get update && apt-get upgrade -y && \
    pip install --no-cache-dir -r requirements.txt

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

EXPOSE 5000

CMD ["python", "app.py"]