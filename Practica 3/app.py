### GESTIÓN DE SISTEMAS DE INFORMACIÓN         ###
### Práctica 3 - Database explorer (Flask API) ###
### Autor - Daniel Callado Martínez            ###
### Fecha - 18/10/2019                         ###

from flask import Flask, render_template, jsonify
import sqlite3
import sys

app = Flask(__name__)
database = None
if len(sys.argv) > 1:
    database = sys.argv[1]

@app.route("/")
def index():
    return render_template('index.html', result = database)

@app.route("/tablas/")
def tablas():
    sql = "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';"
    datos = sqlite3.connect(database).cursor().execute(sql).fetchall()
    return render_template('tablas.html', result = datos)

@app.route("/tablas/<tabla>")
def tablasDatos(tabla):
    sql = "SELECT * from %s;"
    datos = [tabla,sqlite3.connect(database).cursor().execute(sql %(tabla)).fetchall()]
    return render_template('tablasDatos.html', result = datos)

@app.route("/tablas/<tabla>/info")
def tablasInfo(tabla):

    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * from %s;" %(tabla))
    datos = [tabla, len(c.fetchall()), list(map(lambda x: x[0], c.description))]
    return render_template('tablasInfo.html', result = datos)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        app.run()
    else:
        print ("No database found.")
