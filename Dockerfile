FROM python:latest

RUN pip install dotenv psycopg2 flask
RUN pip install waitress

WORKDIR /app
COPY ["insert.py", "main.py", ".env", "./"]
COPY wait-for-it.sh /app

EXPOSE 8080

ENTRYPOINT ["./wait-for-it.sh", "postgres:5432", "--", "waitress-serve", "--listen=0.0.0.0:8080", "main:app"]
