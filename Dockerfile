FROM python:latest

RUN pip install dotenv psycopg2 flask
RUN pip install gunicorn

WORKDIR /app
COPY ["insert.py", "main.py", ".env", "./"]
COPY wait-for-it.sh /app/
RUN chmod +x /app/wait-for-it.sh

EXPOSE 8080

ENTRYPOINT ["/app/wait-for-it.sh", "postgres:5432", "--", "gunicorn", "--bind=0.0.0.0:8080", "main:app"]
