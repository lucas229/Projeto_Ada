from azure.functions import HttpRequest, HttpResponse
import mysql.connector
import json

host='localhost'
user=''
password=''
database='AdaProject'

def main(req: HttpRequest) -> HttpResponse:
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    query = 'SELECT * FROM PRODUTO'

    mycursor = mydb.cursor()
    mycursor.execute(query)
    produtos = mycursor.fetchall()
    mydb.close()

    for i, p in enumerate(produtos):
        produtos[i] = {
            "id": p[0],
            "nome": p[1]
        }

    produtos_json = json.dumps(produtos)

    return HttpResponse(
        produtos_json,
        mimetype="application/json",
        status_code=200
    )
