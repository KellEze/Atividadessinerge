from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/conteudos")
def conteudos():
    return render_template("conteudos.html")


@app.route("/produtos")
def produtos():
    return render_template("produtos.html")


@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# Desafio extra
@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


if __name__ == "__main__":
    app.run(debug=True)

