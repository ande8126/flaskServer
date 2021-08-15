#imports being weird on my vscode, going down an extra line between seemed to help?
import flask

import psycopg2

from flask import request, jsonify

from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# follows my own Postico setup... can change to fit
connection = psycopg2.connect(
    host='Localhost',
    port='5432',
    database='zooapp'
)

@app.route('/api/animals', methods=['GET'])
def list_animals():
    #convert records to objects with RealDictCursor
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    #query text
    postgreSQL_select_Query = "SELECT * FROM animals;"
    #send it over
    cursor.execute(postgreSQL_select_Query)
    #select rows
    animals = cursor.fetchall()
    #response
    return jsonify(animals)

app.run()