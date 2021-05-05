from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mb

def openfile():
    filepath = filedialog.askopenfilenames(initialdir="D:/", filetypes=(("all files", "*.*"),("png files", "*.png"),("jpg files", "*.jpg"),
                                                                    ("pdf files", "*.pdf"),("docx files","*docx")))
    label = Label(text = "")
    label.place(x =10, y=350)
    label.configure(text = filepath)

class document():
    def __init__(self, root):
        self.root = root
        self.root.title("Document Management System")
        self.root.geometry("1020x540")
        self.root.resizable(False, False)

        # set tombol Keluar
        self.imgKeluar = PhotoImage(file='logout.png')
        self.btnKeluar = Button(image=self.imgKeluar, compound='top', command=self.Keluar)
        self.btnKeluar.place(x=970, y=12.5, height=30)
        #===================================

        #Daftar Tabel 
        table1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table1.place(y=50, width=290, height=450)

        name_document= Label(table1, text="Document", bg="white", font=("cambria", 20, "bold"))
        name_document.grid(row=0, columnspan=2, pady=5, padx=75)

        label_name = Label(table1, text="Nama ", bg="white", font=("cambria", 12))
        label_name.grid(row=1,column=0, pady=10, padx=10)

        #Add File
        addfilebtn = Button(table1, text="Add File", command=openfile)
        addfilebtn.place(x=110,y=260)
        #========================================

        #add, clear, edit, save
        table3 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table3.place(y=410, x=10, width=268, height=50)

        addbtn = ttk.Button(table3, text="Add").grid(row=0,column=0, padx=5, pady=10)
        editbtn = ttk.Button(table3, text="Edit").grid(row=0,column=1, padx=6, pady=10)
        deletebtn = ttk.Button(table3, text="Delete").grid(row=0,column=2, padx=6, pady=10)
        clearbtn = ttk.Button(table3, text="Clear").grid(row=0,column=3, padx=6, pady=10)

        #====================================

        table2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table2.place(y=50, x=300, width=719, height=450)
        
        
        searchbtn = Button(text="search")
        searchbtn.place(x=900,y=15)


        entry_name = Entry(table1, bd=3, relief=GROOVE, width=30)
        entry_name.grid(row=1, column=1, pady=10, padx=10)

        search = Entry(bd=3, relief=GROOVE, width=30)
        search.place(x=700,y=14, height=27)

        scroll_y= Scrollbar(table2, orient=VERTICAL)
        document_table = ttk.Treeview(table2, column=("Nama", "Tanggal Upload", "File"), xscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=document_table)

        #Document Table
        document_table.heading("Nama", text="Nama")
        document_table.heading("Tanggal Upload", text="Tanggal Upload")
        document_table.heading("File", text="File")
        document_table["show"]="headings"
        document_table.pack()

        document_table.pack(fill=BOTH, expand=1)

    #Menu Keluar
    def Keluar(self, event=None):
        if mb.askyesno('Konfirmasi', 'Keluar dari program?', parent=self.root):
            self.root.destroy()

if __name__ == '__main__':
    root = Tk()
    root.configure(background="#3cc7f7")
    apk = document(root)
    root.mainloop()
