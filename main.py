import dotenv
import psycopg2
import flask
import os

dotenv.load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

POSTGRES_HOST = "postgres"
POSTGRES_PORT = "5432"
app = flask.Flask(__name__)
conn = psycopg2.connect(database=POSTGRES_DB,
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host=POSTGRES_HOST,
                        port=POSTGRES_PORT)
cursor = conn.cursor()

@app.route('/', methods=['GET'])
def get_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()  # Fetch all rows from the query result

    return flask.jsonify({"contacts": rows})

@app.route('/', methods=['POST'])
def get_contact():
    data = flask.request.get_json()

    if not data:
        return flask.jsonify({"error": "No input data provided"}), 400
    name = data.get("name")
    phone_number = data.get("phone_number")
    email = data.get("email")
    query = "INSERT INTO contacts (name, phone_number, email) VALUES (%s, %s, %s)"
    res = cursor.execute(query, (name, phone_number, email))
    conn.commit()
    return flask.jsonify({"test": str(res)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)