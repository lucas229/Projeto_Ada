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

    query = 'UPDATE PRODUTO SET nome= %s WHERE id = %s'
    valores = (nome, id)

    mycursor = mydb.cursor()
    mycursor.execute(query, valores)
    mydb.commit()
    mydb.close()

    if mycursor.rowcount == 0:
        return HttpResponse(
            "Nenhum produto encontrado com o ID especificado.",
            status_code=404
        )
    
    return HttpResponse(
        "Produto atualizado.",
        status_code=200
    )
