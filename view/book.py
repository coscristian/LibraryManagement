import tkinter as tk
from tkinter import ttk, messagebox #Version of tkinter with better themes for visualization
from controller.book import BookController
from model.book import BookModel
from controller.exceptions import MandatoryField

class BookView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.__book_controller = BookController()
        
        self.geometry("1080x250")
        self.title("Library Management")
        #self.iconbitmap("logo_utp.png")
        
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
        
    def __build_left_frame(self, frame):
        
        ttk.Label(frame, text = "Search").grid(column = 0, row = 0, columnspan = 1)
                    
        # Seach by title button        
        button_search_by_title = ttk.Button(frame, text = "Title", command = self.__open_window_search_by_title)
        button_search_by_title.grid(column = 0, row = 1)
        
        # Search by author button
        button_search_by_author = ttk.Button(frame, text = "Author")
        button_search_by_author.grid(column = 0, row = 2)
        
        # Search by topic button
        button_search_by_topic = ttk.Button(frame, text = "Topic")
        button_search_by_topic.grid(column = 0, row = 3)
        
        button_insert_book = ttk.Button(frame, text = "Insert book", command = self.__open_window_insert_book)
        button_insert_book.grid(column = 0, row = 4)
                                
    def __build_right_frame(self, frame: tk.Frame):
        
        table = ttk.Treeview(frame)
        table.grid(column = 0, row = 0, columnspan = 2)
        
        table['columns'] = ('ID', 'Title', 'Amount', 'Available', 'Topic')
        
        table.heading('#0', text = "", anchor = tk.CENTER)
        table.heading('ID', text = "ID", anchor = tk.CENTER)
        table.heading('Title', text = "Title", anchor = tk.CENTER)
        table.heading('Amount', text = "Amount", anchor = tk.CENTER)
        table.heading('Available', text = "Available", anchor = tk.CENTER)
        table.heading('Topic', text = "Topic", anchor = tk.CENTER)
        
        table.column('#0', width = 0, stretch = tk.NO)
        table.column('ID', anchor = tk.CENTER, width = 40)
        table.column('Title', anchor = tk.CENTER, width = 300)
        table.column('Amount', anchor = tk.CENTER, width = 80)
        table.column('Available', anchor = tk.CENTER, width = 80)
        table.column('Topic', anchor = tk.CENTER, width = 300)
        
        button1 = ttk.Button(frame, text = "Lend book")
        button1.grid(column = 0, row = 1)
        
        button2 = ttk.Button(frame, text = "Show Info")
        button2.grid(column = 1, row = 1)        

    def __open_window_search_by_title(self):
        
        def search_by_title():
            books = self.__book_controller.list_by_title(self.__book_title.get())
            search_by_title_window.destroy()
            print(books)
                    
        search_by_title_window = tk.Tk()
        search_by_title_window.geometry("350x100")
        search_by_title_window.title("Seaching book")
        
        frame = tk.Frame(search_by_title_window)
        frame.grid(column = 0, row = 0)
        
        ttk.Label(frame, text = "Title").grid(column = 0, row = 0, padx=25, pady=40)
        self.__book_title = tk.StringVar()
        ttk.Entry(frame, textvariable = self.__book_title).grid(column = 1, row = 0, padx = 5, pady = 5)
        
        button_search_book = ttk.Button(frame, text = "Search", command = search_by_title)
        button_search_book.grid(column = 2, row = 0, padx = 5, pady = 5)
        
        #self.mainloop()
        
    # TODO: Function def __open_window_search_by_author(self)
    
    # TODO: Function def __open_window_search_by_topic(self)

    def __open_window_insert_book(self):
        
        def are_valid_fields(title: str, amount: int, amount_available: int, topic: str, author) -> bool:
            empty_field = len(title) == 0 or amount == 0 or amount_available == 0 or len(topic) == 0 or len(author) == 0
            if not empty_field:
                return True
            return False
        
        def insert_book(title_entry, amount_entry, amount_available_entry, topic_entry, author_entry):
            # TODO: Validar errores con try y en caso de error lanzar la excepción
            
            title = title_entry.get()
            amount = amount_entry.get()
            available = amount_available_entry.get()
            topic = topic_entry.get()
            author = author_entry.get()
            
            #CHECK HERE
            try:
                if are_valid_fields(title, amount, available, topic, author):
                    self.__book_controller.insert(BookModel(title, int(amount), int(available), topic, author))
                    insert_book_window.destroy() 
                    messagebox.showinfo("Inserting book","Book added sucesfully!!")
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
        #__new_book_title = tk.StringVar()
        title_entry = ttk.Entry(frame)
        title_entry.grid(column = 1, row = 0, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Amount").grid(column = 0, row = 1, padx=25, pady=5)
        #self.__new_book_amount = tk.IntVar()
        amount_entry = ttk.Entry(frame)
        amount_entry.grid(column = 1, row = 1, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Amount available").grid(column = 0, row = 2, padx=25, pady=5)
        #self.__new_book_amount_av = tk.IntVar()
        amount_available_entry = ttk.Entry(frame)
        amount_available_entry.grid(column = 1, row = 2, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Topic").grid(column = 0, row = 3, padx=25, pady=5)
        #self.__new_book_topic = tk.StringVar()
        topic_entry = ttk.Entry(frame)
        topic_entry.grid(column = 1, row = 3, padx = 5, pady = 5)
        
        ttk.Label(frame, text = "Author").grid(column = 0, row = 4, padx=25, pady=5)
        #self.__new_book_author = tk.StringVar()
        author_entry = ttk.Entry(frame)
        author_entry.grid(column = 1, row = 4, padx = 5, pady = 5)
                
        button_insert_book = ttk.Button(frame, text = "Insert", command = lambda title = title_entry, amount = amount_entry, available = amount_available_entry, topic = topic_entry, author = author_entry : insert_book(title, amount, available, topic, author))
        button_insert_book.grid(column = 1, row = 5, padx = 5, pady = 5)
        
        #self.mainloop()
        

    def start_execution(self):
        self.mainloop()
        
