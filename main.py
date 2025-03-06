from dotenv import load_dotenv
from psycopg2 import connect
from flask import Flask, request, jsonify
import os

load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")

app = Flask(__name__)
conn =  connect(database=POSTGRES_DB,
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host=POSTGRES_HOST,
                        port=POSTGRES_PORT)
cursor = conn.cursor()

@app.route('/', methods=['GET'])
def get_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    return jsonify({"contacts": rows})

@app.route('/', methods=['POST'])
def get_contact():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400
    name = data.get("name")
    if not name:
        return jsonify({"error": "name is a mandatory parameter"}), 400

    phone_number = data.get("phone_number")
    email = data.get("email")

    query = "INSERT INTO contacts (name, phone_number, email) VALUES (%s, %s, %s)"
    res = cursor.execute(query, (name, phone_number, email))
    conn.commit()

    return jsonify({"test": str(res)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)