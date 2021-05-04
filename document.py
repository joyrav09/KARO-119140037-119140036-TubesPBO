from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

class document():
    def __init__(self,root):
        self.root = root
        self.root.title("Document Management System")
        self.root.geometry("1020x540")
        self.root.resizable(False, False)

        # set tombol Keluar
        self.imgKeluar = PhotoImage(file='png\logout.png')
        self.btnKeluar = Button(image=self.imgKeluar, compound='top', command=self.Keluar)
        self.btnKeluar.place(x=970, y=12.5, height=30)

        table1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table1.place(y=50, width=290, height=450)

        table2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table2.place(y=50, x=300, width=719, height=450)
        
        
        search = Entry(bd=3, relief=GROOVE, width=30)
        search.place(x=700,y=14, height=27)

        searchbtn = Button(text="search")
        searchbtn.place(x=900,y=15)

        scroll_y= Scrollbar(table2, orient=VERTICAL)
        document_table = ttk.Treeview(table2, column=("Nama", "Tanggal Upload", "File"), xscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=document_table)

        document_table.heading("Nama", text="Nama")
        document_table.heading("Tanggal Upload", text="Tanggal Upload")
        document_table.heading("File", text="File")
        document_table["show"]="headings"
        document_table.pack()

        document_table.pack(fill=BOTH, expand=1)

    def Keluar(self, event=None):
        if mb.askyesno('Konfirmasi', 'Keluar dari program?', parent=self.root):
            self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.configure(background="#3cc7f7")
    apk = document(root)
    root.mainloop()
