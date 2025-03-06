FROM python:latest

RUN pip install dotenv psycopg2 flask
RUN pip install gunicorn

WORKDIR /app

COPY ["main.py", ".env", "./"]

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "main:app"]