from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
import logging

app = Flask(__name__)
logging.basicConfig(filename='error.log', level=logging.DEBUG)


@app.route("/")
def index():
    return "Index Flask App"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect("/")
    else:
        return render_template('login.html')


@app.route("/juego", methods=["POST"])
def agregar_juego():
    try:
        token = request.headers.get("token")
        app.logger.debug(f"Token {token}")
        info = request.get_json()
        nombre = info["nombre"]
        precio = info["precio"]
        return f"Nombre {nombre}, Precio {precio}"
    except:
        return abort(404)


@app.route("/juego/<int:id>")
def obtener_juego(id):
    return f"ID juego {id}"


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("error.html", error=error)
