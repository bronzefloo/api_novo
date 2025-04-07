# Api Livros Doados VnW

Essa é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai na Web, ela permite cadastrar e listar os livros doados. 

## Como rodar o projeto?

1. Faça o clone do repositório:
``` bash
git clone <LINK_DO_REPOSITÓRIO>
cd nome_do_projeto
```

2. Criar um ambiente virtual (Obrigatório):
```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:
``` bash
pip install -r requirements.txt
```

4. Inicie o servidor: 
``` bash
python app.py
```

## Endpoints

### POST /doar

> A API estará disponível em http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoint para cadastro das informações do livro doado.

**Envio (JSON)**
```json
{
    "titulo":"Harry Potter e o enigma do príncipe",
    "categoria":"Fantasia",
    "autor":"J.K Rowling",
    "image_url":"https://..."
}
```
### Resposta (JSON)
Caso o livro seja cadastrado com sucesso, a API retornará uma resposta com os dados do livro:
```json
{
    "id": 1,
    "titulo": "Harry Potter e o enigma do príncipe",
    "categoria": "Fantasia",
    "autor": "J.K. Rowling",
    "image_url": "https://..."
}
```

### ERRO
Se ocorrer um erro na requisição, a API retornará uma mensagem de erro com o código de status.
```json
{
    "Erro": "Os campos 'titulo', 'categoria', 'autor' e 'image_url' são obrigatórios!"
}
```

### GET / livros
Este endpoint permite listar todos os livros cadastrados.

### Resposta (JSON)
A resposta será uma lista de livros registrados:

```json
[
    {
        "id": 1,
        "titulo": "Harry Potter e o enigma do príncipe",
        "categoria": "Fantasia",
        "autor": "J.K. Rowling",
        "image_url": "https://..."
    },
    {
        "id": 2,
        "titulo": "O Senhor dos Anéis",
        "categoria": "Fantasia",
        "autor": "J.R.R. Tolkien",
        "image_url": "https://..."
    }
]
```
### Como o banco de dados funciona
O banco de dados utilizado é o SQLite, e os dados são armazenados em um arquivo chamado database.db 

A tabela LIVROS armazena as seguintes informações de cada livro:

- id: Identificador único do livro (chave primária).

- titulo: Título do livro.

- categoria: Categoria ou gênero do livro.

- autor: Nome do autor do livro.

- image_url: URL da imagem da capa do livro.
