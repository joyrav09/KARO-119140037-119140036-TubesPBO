from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mb
import pymysql

class document():
    def __init__(self, root):
        self.root = root
        self.root.title("Document Management System")
        self.root.geometry("1020x540")
        self.root.resizable(False, False)


        self.var_name = StringVar()
        self.var_nim = StringVar()
        self.var_prodi = StringVar()

        # set tombol Keluar
        self.imgKeluar = PhotoImage(file='logout.png')
        self.btnKeluar = Button(image=self.imgKeluar, compound='top', command=self.Keluar)
        self.btnKeluar.place(x=970, y=12.5, height=30)
        #===================================

        #Daftar Tabel 
        table1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table1.place(y=50, width=290, height=450)

        name_document= Label(table1, text="DOKUMEN", bg="white", font=("cambria", 20, "bold"))
        name_document.grid(row=0, columnspan=2, pady=5, padx=75)

        label_name = Label(table1, text="Nama ", bg="white", font=("cambria", 12))
        label_name.grid(row=1,column=0, pady=10, padx=10, sticky="w")
        label_nim = Label(table1, text="NIM ", bg="white", font=("cambria", 12))
        label_nim.grid(row=2,column=0, pady=10, padx=10, sticky="w")
        label_prodi = Label(table1, text="Prodi", bg="white", font=("cambria", 12))
        label_prodi.grid(row=3,column=0, pady=10, padx=10, sticky="w")

        #Add File
        self.addfilebtn = Button(table1, text="Add File", command=self.openfile)
        self.addfilebtn.place(x=110,y=260)
        #========================================

        #add, clear, edit, save
        table3 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table3.place(y=410, x=10, width=268, height=50)

        addbtn = Button(table3, text="Tambah", command=self.add_document).grid(row=0,column=0, padx=9, pady=10)
        editbtn = Button(table3, text="Edit", command=self.edit_data).grid(row=0,column=1, padx=9, pady=10)
        deletebtn = Button(table3, text="Hapus", command=self.delete_data).grid(row=0,column=2, padx=9, pady=10)
        clearbtn = Button(table3, text="Bersihkan", command=self.clear).grid(row=0,column=3, padx=9, pady=10)

        #====================================

        table2 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        table2.place(y=50, x=300, width=719, height=450)
        
        
        searchbtn = Button(text="Cari")
        searchbtn.place(x=900,y=15)


        entry_name = Entry(table1,textvariable=self.var_name, bd=3, relief=GROOVE, width=30)
        entry_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        entry_nim = Entry(table1,textvariable=self.var_nim, bd=3, relief=GROOVE, width=30)
        entry_nim.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        entry_prodi = Entry(table1,textvariable=self.var_prodi, bd=3, relief=GROOVE, width=30)
        entry_prodi.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        
        search = Entry(bd=3, relief=GROOVE, width=30)
        search.place(x=700,y=14, height=27)

        scroll_x= Scrollbar(table2, orient=HORIZONTAL)
        scroll_y= Scrollbar(table2, orient=VERTICAL)  
        self.document_table = ttk.Treeview(table2, column=("Nama", "NIM", "Prodi", "File"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)    
        scroll_y.config(command=self.document_table.yview)
        scroll_x.config(command=self.document_table.xview)

        #Document Table
        self.document_table.heading("Nama", text="Nama")
        self.document_table.heading("NIM", text="NIM")
        self.document_table.heading("Prodi", text="Prodi")
        self.document_table.heading("File", text="File")
        self.document_table["show"]="headings"
        self.document_table.column("Nama", width=100)
        self.document_table.column("NIM", width=100)
        self.document_table.column("Prodi", width=100)
        self.document_table.column("File", width=100)
        self.document_table.pack(fill=BOTH, expand=1)
        self.document_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_data()

    def openfile(self, event=None):
        self.filepath = filedialog.askopenfilenames(initialdir="D:/", filetypes=(("all files", "*.*"),("png files", "*.png"),("jpg files", "*.jpg"),
                                                                    ("pdf files", "*.pdf"),("docx files","*docx")))
        self.label = Label(text = "")
        self.label.grid(padx =10, pady=350)
        self.label.configure(text = self.filepath, bg="yellow")
        print('Selected:', self.filepath)

    def add_document(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="document")
        cur=con.cursor()
        cur.execute("insert into document values(%s, %s, %s, %s)",(self.var_name.get(),
                                                                   self.var_nim.get(),
                                                                   self.var_prodi.get(),
                                                                   self.addfilebtn
                                                                   ))
        con.commit()
        self.show_data()
        self.clear()
        con.close()

    def show_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="document")
        cur=con.cursor()
        cur.execute("select * from document")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.document_table.delete(*self.document_table.get_children())
            for row in rows:
                self.document_table.insert("", END, values=row)
            con.commit()
        con.close()
    
    def clear(self):
        self.var_name.set("")
        self.var_nim.set("")
        self.var_prodi.set("")

    def get_cursor(self, ev):
        cursor_row=self.document_table.focus()
        content=self.document_table.item(cursor_row)
        row=content["values"]
        self.var_name.set(row[0])
        self.var_nim.set(row[1])
        self.var_prodi.set(row[2])

    def edit_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="document")
        cur=con.cursor()
        cur.execute("update document set nama=%s, prodi=%s, file=%s where nim=%s",(self.var_name.get(),
                                                                                  self.var_prodi.get(),
                                                                                  self.addfilebtn,
                                                                                  self.var_nim.get()
                                                                                  ))
        con.commit()
        self.show_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="document")
        cur=con.cursor()
        cur.execute("delete from document where nim=%s", self.var_nim.get())
        con.commit()
        con.close()
        self.show_data()
        self.clear()

     #Menu Keluar
    def Keluar(self, event=None):
        if mb.askyesno('Konfirmasi', 'Keluar dari program?', parent=self.root):
            self.root.destroy()
    

if __name__ == '__main__':
    root = Tk()
    root.configure(background="#3cc7f7")
    apk = document(root)
    root.mainloop()
