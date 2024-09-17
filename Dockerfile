FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV POSTGRES_DB=products
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_HOST=db

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]