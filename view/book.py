import tkinter  as tk
from tkinter import ttk, messagebox #Version of tkinter with better themes for visualization
from controller.book import BookController
from model.book import BookModel
from controller.exceptions import MandatoryField

class BookView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.__book_controller = BookController()
        
        self.geometry("1250x250")
        self.title("Library Management")
        self.resizable(False,False)
        
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 2)
        
        # Creating left frame
        left_frame = tk.Frame(self)
        self.__build_left_frame(left_frame)
        left_frame.grid(column = 0, row = 0)
        
        # Creating right frame
        right_frame = tk.Frame(self)
        self.__build_right_frame(right_frame)
        right_frame.grid(column = 1, row = 0)
        
        self.__load_table(None)
        
    def search_by_title(self, user_entry: ttk.Entry):
        title = user_entry.get()
        self.books = self.__book_controller.list_by_title(title)
        self.__load_table(self.books)
        self.window_search.destroy()
        
            
    def search_by_author(self, user_entry: ttk.Entry):
        self.books = self.__book_controller.list_by_author(user_entry.get())
        self.__load_table(self.books)
        self.window_search.destroy()
            
    def search_by_topic(self, user_entry: ttk.Entry):
        self.books = self.__book_controller.list_by_topic(user_entry.get())
        self.__load_table(self.books)
        self.window_search.destroy()
        
    def __build_left_frame(self, frame):
        
        ttk.Label(frame, text = "Search By").grid(column = 0, row = 0, columnspan = 1)
                    
        # Seach by title button        
        button_search_by_title = ttk.Button(frame, text = "Title",
                                            command = lambda window_title = "Searching book by title", window_label_text = "Title", window_button_text = "Search",
                                            window_button_event = self.search_by_title:
                                                self.__open_window_search(window_title, window_label_text, window_button_text, window_button_event)
                                            )
        button_search_by_title.grid(column = 0, row = 1, pady = 7)
        
        # Search by author button
        button_search_by_author = ttk.Button(frame, text = "Author",
                                            command = lambda window_title = "Searching book by author", window_label_text = "Author", window_button_text = "Search",
                                            window_button_event = self.search_by_author:
                                                self.__open_window_search(window_title, window_label_text, window_button_text, window_button_event)
                                            )
        button_search_by_author.grid(column = 0, row = 2)
        
        # Search by topic button
        button_search_by_topic = ttk.Button(frame, text = "Topic",
                                            command = lambda window_title = "Searching book by topic", window_label_text = "Topic", window_button_text = "Search",
                                            window_button_event = self.search_by_topic:
                                                self.__open_window_search(window_title, window_label_text, window_button_text, window_button_event)
                                            )
        button_search_by_topic.grid(column = 0, row = 3, pady = 7)
        
        button_insert_book = ttk.Button(frame, text = "Insert book", command = self.__open_window_insert_book)
        button_insert_book.grid(column = 0, row = 4, pady = 7)
        
        button_restart_table= ttk.Button(frame, text = "Restart table", command = lambda : self.__load_table(None))
        button_restart_table.grid(column = 0, row = 5, pady = 7)
                                
    def __build_right_frame(self, frame: tk.Frame):
        
        self.__table = ttk.Treeview(frame)
        self.__table.grid(column = 0, row = 0, columnspan = 2, pady=7)
        
        self.__table['columns'] = ('ID', 'Title', 'Amount', 'Available', 'Topic', 'Author')
        
        self.__table.heading('#0', text = "", anchor = tk.CENTER)
        self.__table.heading('ID', text = "ID", anchor = tk.CENTER)
        self.__table.heading('Title', text = "Title", anchor = tk.CENTER)
        self.__table.heading('Amount', text = "Amount", anchor = tk.CENTER)
        self.__table.heading('Available', text = "Available", anchor = tk.CENTER)
        self.__table.heading('Topic', text = "Topic", anchor = tk.CENTER)
        self.__table.heading('Author', text = "Author", anchor = tk.CENTER)
        
        self.__table.column('#0', width = 0, stretch = tk.NO)
        self.__table.column('ID', anchor = tk.E, width = 40)
        self.__table.column('Title', anchor = tk.CENTER, width = 300)
        self.__table.column('Amount', anchor = tk.E, width = 80)
        self.__table.column('Available', anchor = tk.E, width = 80)
        self.__table.column('Topic', anchor = tk.CENTER, width = 300)
        self.__table.column('Author', anchor = tk.CENTER, width = 300)
        
    def __open_window_search(self, window_title: str, label_text: str, button_text: str, button_event):
                    
        self.window_search = tk.Tk()
        self.window_search.geometry("380x100")
        self.window_search.title(window_title)

        frame = tk.Frame(self.window_search)
        frame.grid(column = 0, row = 0)
        
        ttk.Label(frame, text = label_text).grid(column = 0, row = 0, padx=25, pady=40)
        entry = ttk.Entry(frame)
        entry.grid(column = 1, row = 0, padx = 5, pady = 5)
        
        button_search_book = ttk.Button(frame, text = button_text, command = lambda user_entry = entry : button_event(user_entry))
        button_search_book.grid(column = 2, row = 0, padx = 5, pady = 5)
        
    def __open_window_insert_book(self):
        
        def are_valid_fields(title: str, amount: int, amount_available: int, topic: str, author) -> bool:
            empty_field = len(title) == 0 or amount == 0 or amount_available == 0 or len(topic) == 0 or len(author) == 0
            if not empty_field:
                return True
            return False
        
        def insert_book(title_entry, amount_entry, amount_available_entry, topic_entry, author_entry):
        
            title = title_entry.get()
            amount = amount_entry.get()
            available = amount_available_entry.get()
            topic = topic_entry.get()
            author = author_entry.get()
            
            try:
                if are_valid_fields(title, amount, available, topic, author):
                    self.__book_controller.insert(BookModel(0, title, int(amount), int(available), topic, author))
                    insert_book_window.destroy() 
                    messagebox.showinfo("Inserting book","Book added sucesfully!!")
                    self.__load_table(None)
                else:
                    raise MandatoryField("Los campos son obligatorios.")
            except ValueError:
                messagebox.showerror("ERROR: Please input a correct int value")
            except MandatoryField as mandatory_field:
                messagebox.showerror(f"ERROR: {mandatory_field.get_message()}")
                
        insert_book_window = tk.Tk()
        insert_book_window.geometry("350x210")
        insert_book_window.title("Inserting book")
        
        frame = tk.Frame(insert_book_window)
        frame.grid(column = 0, row = 0)
        
        ttk.Label(frame, text = "Title").grid(column = 0, row = 0, padx=25, pady=5)
        title_entry = ttk.Entry(frame)
        title_entry.grid(column = 1, row = 0, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Amount").grid(column = 0, row = 1, padx=25, pady=5)
        amount_entry = ttk.Entry(frame)
        amount_entry.grid(column = 1, row = 1, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Amount available").grid(column = 0, row = 2, padx=25, pady=5)
        amount_available_entry = ttk.Entry(frame)
        amount_available_entry.grid(column = 1, row = 2, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Topic").grid(column = 0, row = 3, padx=25, pady=5)
        topic_entry = ttk.Entry(frame)
        topic_entry.grid(column = 1, row = 3, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Author").grid(column = 0, row = 4, padx=25, pady=5)
        author_entry = ttk.Entry(frame)
        author_entry.grid(column = 1, row = 4, padx = 5, pady = 5)
                
        button_insert_book = ttk.Button(frame, text = "Insert", command = lambda title = title_entry, amount = amount_entry, available = amount_available_entry, topic = topic_entry, author = author_entry : insert_book(title, amount, available, topic, author))
        button_insert_book.grid(column = 1, row = 5, padx = 5, pady = 5)
        
    def __load_table(self, books):
        if books == None:
            books = self.__book_controller.list_books()
        
        # Clear the table elements
        for item in self.__table.get_children(""):
            self.__table.delete(item)
        
        for book in books:
            book_id = book.get_id()
            self.__table.insert(parent = '', index = book_id, iid = book_id, text = "", values = (book_id, book.get_title(), book.get_amount(), book.get_amount_available(), book.get_topic(), book.get_author()))
            
    def start_execution(self):
        self.mainloop()
        
