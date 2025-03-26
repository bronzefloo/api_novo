import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def init_db():
    # Conectamos ao banco de dados SQLite e usamos "with" para garantir que a conexão seja fechada corretamente após a execução
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para criar a tabela LIVROS, caso ela ainda não exista
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    autor TEXT NOT NULL,
                    image_url TEXT NOT NULL
                )
            """
        )  # A execução desse comando cria a tabela caso ela ainda não exista, garantindo que nossa estrutura de banco esteja configurada


# Chamamos a função para inicializar o banco de dados quando o programa for executado
init_db()


@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"Erro": "Os campos 'titulo', 'categoria', 'autor' e 'image_url' são obrigatórios!"}), 400

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url)
            VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
""")
        conn.commit()

        return jsonify({"messagem": "Livro doado com sucesso!"}), 201


@app.route("/livros", methods=["GET"])
def listar_livros():

    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []

        for item in livros:
            dicionario_livros = {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4]
            }
            livros_formatados.append(dicionario_livros)

    return jsonify(livros_formatados), 200


if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração (nesse modo nossa API responde automaticamente a qualquer atualização que fizermos no código)
    app.run(debug=True)
