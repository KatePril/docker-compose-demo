from flask import jsonify

def insert_data(data, cursor, conn):
    name = data.get("name")
    if not name:
        return jsonify({"error": "name is a mandatory parameter"}), 400
    phone_number = data.get("phone_number")
    email = data.get("email")
    d = {"name": name, "phone_number": phone_number, "email": email}

    output = insert_partial_data(param1="phone_number", param2="email", d=d,
                                 query="INSERT INTO contacts (name, email) VALUES (%s, %s)",
                                 cursor=cursor, conn=conn)
    if output:
        return output, 200

    output = insert_partial_data(param1="email", param2="phone_number", d=d,
                                 query="INSERT INTO contacts (name, phone_number) VALUES (%s, %s)",
                                 cursor=cursor, conn=conn)
    if output:
        return output, 200

    query = "INSERT INTO contacts (name, phone_number, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, phone_number, email))
    conn.commit()
    return jsonify({"inserted": d}), 200

def insert_partial_data(param1, param2, d, query, cursor, conn):
    if not d[param1]:
        del d[param1]
        if not d[param2]:
            query = "INSERT INTO contacts (name) VALUES (%s)"
            cursor.execute(query, d["name"])
            del d[param2]
        else:
            cursor.execute(query, (d["name"], d[param2]))
        conn.commit()
        return jsonify({"inserted": d})
    else:
        return None