import tkinter as tk
from tkinter import ttk #Version of tkinter with better themes for visualization
from controller.book import BookController

class BookView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("640x480")
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
                
    def __build_right_frame(self, frame: tk.Frame):
        
        table = ttk.Treeview(frame)
        table.grid(column = 0, row = 0, columnspan = 2)
        
        button1 = ttk.Button(frame, text = "Lend book")
        button1.grid(column = 0, row = 1)
        
        button2 = ttk.Button(frame, text = "Show Info")
        button2.grid(column = 1, row = 1)        

    def __open_window_search_by_title(self):
        
        def search_by_title():
            book_controller = BookController()
            books = book_controller.list_by_title(self.__book_title.get())
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
        
        self.mainloop()

    def start_execution(self):
        self.mainloop()
        
