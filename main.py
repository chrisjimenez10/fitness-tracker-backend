from flask import Flask, request, jsonify
import pymysql.cursors

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        password='cratose@41795',
        user='root',
        database='fitness-exercises',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Hello, Welcome to Fitness Tracker"

@app.route("/exercises")
def get_exercises():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM exercises;")
        exercises = cursor.fetchall()
        connection.close()
        return jsonify(exercises), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



app.run(port=3005)

