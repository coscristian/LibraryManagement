import mysql.connector

def connect():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Quesada-123",
        database = "Library"
    )
    return db
    
