from controller.connection import connect
from model.book import BookModel

class BookController:
    def list_books():
        sql = "SELECT * FROM Book"
        
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall() #Get all the rows of the previous querie
        db.close()
        
        books = list(map(lambda t: BookModel(t[0], t[1], t[2], t[3], t[4], []), results))
        return books  
    
    def insert(self, book: BookModel):
        sql = "INSERT INTO Book (title, amount, amount_available, topic, author) VALUES ('%s', %d, %d, '%s', '%s')" % (book.get_title(), book.get_amount(), book.get_amount_available(), book.get_topic(), book.get_author())
        
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        
    def update(self, book: BookModel):
        sql = "UPDATE Book SET title = '%s', amount = %d, amount_available = %d, topic = '%s' WHERE id = %d" % (book.get_title(), book.get_amount(), book.get_amount_available(), book.get_topic(), book.get_id())
        
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        
    def delete(self, book_id: int):
        sql = "DELETE FROM Book WHERE id = %d" % (book_id)
        
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        
    def list_by_author(self, author: str):
        sql = "SELECT * FROM Book WHERE author = '%s'" % (author)
        
        db = connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall() #Get all the rows of the previous querie
        
        # Must receive the data and parse them into a bookModel object to show them
        # Must return 'that
        
        db.close()        
    
    def list_by_key_word(self, key_word: str):
        pass
    
    def list_by_topic(self, topic: str):
        pass
        