from azure.functions import HttpRequest, HttpResponse
import mysql.connector
import json

host='localhost'
user=''
password=''
database='AdaProject'

def main(req: HttpRequest) -> HttpResponse:
    id = req.route_params.get('id')
    if not id:
        return HttpResponse(
            "Forneça o ID do produto como parâmetro.",
            status_code=400
        )

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    query = 'SELECT * FROM PRODUTO WHERE id = %s'
    valores = (id,)

    mycursor = mydb.cursor()
    mycursor.execute(query, valores)
    produto = mycursor.fetchone()
    mydb.close()

    if produto is None:
        return HttpResponse(
            "Produto não encontrado.",
            status_code=404
        )

    produto = {
        "id": produto[0],
        "nome": produto[1]
    }

    produto_json = json.dumps(produto)

    return HttpResponse(
        produto_json,
        mimetype="application/json",
        status_code=200
    )
