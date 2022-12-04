import tkinter as tk

class BookView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry("640x480")
        self.title("Library Management")
        #self.iconbitmap("logo_utp.png")
        
    def start_execution(self):
        self.mainloop()