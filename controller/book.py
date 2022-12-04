from controller.connection import connect

class BookController:
    def list_books():
        sql = "SELECT * FROM Book"
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall() #Get all the rows of the previous querie
        
        
            
        
        db.close()
        