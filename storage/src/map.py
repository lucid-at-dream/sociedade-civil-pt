from flask import Flask

app = Flask(__name__)

@app.route("/event", methods=["PUT"])
def create_event():
    return "<p>Hello, World!</p>"

@app.route("/event", methods=["GET"])
def read_event():
    return "<p>Hello, World!</p>"

@app.route("/event", methods=["POST"])
def update_event():
    return "<p>Hello, World!</p>"

@app.route("/event", methods=["DELETE"])
def delete_event():
    return "<p>Hello, World!</p>"