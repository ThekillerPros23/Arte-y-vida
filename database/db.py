import pymysql 

def connect():
    db = pymysql.connect(host = "arteyvida.mysql.database.azure.com", user="arteyvida", password="zX9E^Pt8v9V3", db = None)
    cursor = db.cursor()
    cursor.execute("show databases")
    baseDatos = cursor.fetchmany()
    for databases in baseDatos:
        print(databases)
    db.commit()
    db.close()
    