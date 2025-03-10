from flask import Flask

app = Flask(__name__)

@app.route("/pagar")
def exibir_mensagem():
    return "<h1>Pagamento realizado com sucesso!</h1>"

@app.route("/calote")
def exibir_mensagem_calote():
    return "<h2>oii tudo bem</h2>"

if __name__ == "__main__":
    app.run(debug=True)
