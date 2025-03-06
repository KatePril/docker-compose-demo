FROM python:latest

RUN pip install dotenv psycopg2 flask

RUN pip install waitress

WORKDIR /app

COPY ["main.py", ".env", "./"]

EXPOSE 8080

COPY wait-for-it.sh /app/
ENTRYPOINT ["./wait-for-it.sh", "postgres:5432", "--", "waitress-serve", "--listen=0.0.0.0:8080", "main:app"]
