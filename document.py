from tkinter import *
from tkinter import ttk

class document():
    def __init__(self,root):
        self.root = root
        self.root.title("Document Management System")
        self.root.geometry("720x540")
        self.root.resizable(False, False)
        
        table = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table.place( y=50, width=719, height=400)
        
        
        search = Entry(bd=7, relief=GROOVE)
        search.grid(row=0, column=2, padx=10,pady=10)

        searchbtn = Button(text="search")
        searchbtn.grid(row=0, column=3, padx=10,pady=10)

        scroll_y= Scrollbar(table, orient=VERTICAL)
        document_table = ttk.Treeview(table, column=("No", "NIM", "Nama", "Prodi"),xscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=document_table)

        document_table.heading("No", text="No")
        document_table.heading("NIM", text="NIM")
        document_table.heading("Nama", text="Nama")
        document_table.heading("Prodi", text="Prodi")
        document_table["show"]="headings"
        document_table.pack()
        document_table.column("No", width=50)
        document_table.column("NIM", width=190)
        document_table.column("Nama", width=230)
        document_table.column("Prodi", width=220)
        document_table.pack(fill=BOTH, expand=1)


root = Tk()
apk = document(root)
root.mainloop()
