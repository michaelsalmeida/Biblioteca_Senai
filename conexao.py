def conex():

    import mysql.connector

    mydb = mysql.connector.connect(

    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "biblioteca"

    )

    if mydb.is_connected():
        return mydb
    else:
        import sys
        print('Conexão com o banco falhou')
        sys.exit()
