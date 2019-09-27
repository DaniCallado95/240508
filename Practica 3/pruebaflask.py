from flask import Flask
import sqlite3
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/tabla/")
def hello2():
    conn = sqlite3.connect("ejemplo.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Clientes;")
    datos = json.dumps(c.fetchall())
    return datos

if __name__ == "__main__":
    app.run()
