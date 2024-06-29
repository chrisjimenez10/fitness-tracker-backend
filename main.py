from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return "Hello, Welcome to Fitness Tracker"

app.run(port=3005)

