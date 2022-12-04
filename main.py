from controller.book import BookController
from view.book import BookView

window = BookView()
window.start_execution()


book_controller = BookController()
books = book_controller.list_books()

print(books)
