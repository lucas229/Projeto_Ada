from azure.functions import HttpRequest, HttpResponse
import mysql.connector

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

    query = 'DELETE FROM PRODUTO WHERE id = %s'
    valores = (id,)

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
        status_code=204
    )
