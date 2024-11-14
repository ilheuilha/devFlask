from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/olamundo")
def hello_world():
    return "<p>Hello, World - Varias versões !</p>"


@app.route("/bemvindo/<usuario>/<int:idade>/<float:altura>")
def bem_vindo(usuario, idade, altura):
    return {"Nome": usuario, "Idade": idade, "Altura": altura}

    # f"<h2>Olá, {usuario.upper()}, seja bem vindo ! Sua idade é: {idade} </h2>"


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        return "This is a GET"
    else:
        return "This is a POST"


with app.test_request_context():
    print(url_for("bem_vindo", usuario="walter", idade=39, altura=1.72))
    print(url_for("projects"))
    print(url_for("about", next="/"))


# poetry run flask --app src.app run --debug /* rodar o flask
