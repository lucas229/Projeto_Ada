from azure.functions import HttpRequest, HttpResponse
import mysql.connector

host='localhost'
user=''
password=''
database='AdaProject'

def main(req: HttpRequest) -> HttpResponse:
    try:
        request_json = req.get_json()
        id = request_json.get('id')
        nome = request_json.get('nome')
    except:
        return HttpResponse(
            'Forneça um JSON válido.',
            status_code=400
        )

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    query = 'INSERT INTO PRODUTO (id, nome) VALUES (%s, %s)'
    valores = (id, nome)

    mycursor = mydb.cursor()
    mycursor.execute(query, valores)
    mydb.commit()
    mydb.close()

    return HttpResponse(
        "Produto criado.",
        status_code=201
    )
