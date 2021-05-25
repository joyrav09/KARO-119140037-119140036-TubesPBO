from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as mb
import pymysql
import tkinter.ttk as ttk 
import os


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (MenuUtama, program):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(MenuUtama)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class MenuUtama(ttk.Frame):
    def __init__(self, root, controller):
        self.controller = controller
        ttk.Frame.__init__(self, root)
        self.make_widget()

    def make_widget(self):
        self.cvs = Canvas(self, width="1020", height="540", background="#D9D9D9")
       

        # demo button to change page
        namaLabel = Label(self.cvs, text="SELAMAT DATANG", font=("Cambria", 30, "bold"), background="#D9D9D9")
        namaLabel.place(x=345, y=190)
        btnMasuk = Button(self.cvs, text="Masuk", command=lambda: self.controller.show_frame(program), 
                            bg="#A1A5A6", font=("Cambria", 12, "bold"))
        btnMasuk.place(x=460, y=250, width="100", height="35")
        self.cvs.pack()

class document(ttk.Frame):
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller   
        ttk.Frame.__init__(self, root)
        self.make_widget()

    def make_widget(self):
        self.var_name = StringVar()
        self.var_nim = StringVar()
        self.var_prodi = StringVar()
        self.var_umur = StringVar() 
        self.var_agama = StringVar()
        self.var_nohp = StringVar()

        self.var_search = StringVar()

        #TAMPILAN UTAMA
        searchbtn = Button(self, text="Cari", command=self.search_data, bg="#A1A5A6")
        searchbtn.place(x=849,y=15)
        showallhbtn = Button(self, text="Semua", command=self.show_data, bg="#A1A5A6")
        showallhbtn.place(x=890,y=15)
        
        search = Entry(self, textvariable=self.var_search, bd=3, relief=GROOVE, width=30)
        search.place(x=650,y=14, height=27)
        
        downloadbtn = Button(self, text="Download", command=self.download, bg="#A1A5A6")
        downloadbtn.place(x=550, y=15)
        deletebtn = Button(self, text="Hapus", command=self.delete_data, bg="#A1A5A6")
        deletebtn.place(x=490,y=15)

        btnkembali = Button(self, text='Kembali',
                             command=lambda: self.controller.show_frame(MenuUtama), bg="#A1A5A6")
        btnkembali.place(x=950, y=14.5)
        #===================================

        #SET TOMBOL KELUAR
        #self.imgKeluar = PhotoImage(file='logout.png')
        #self.btnKeluar = Button(image=self.imgKeluar, compound='top', command=self.close)
        #self.btnKeluar.place(x=970, y=12.5, height=30)
        #===================================

        #TABEL 1
        table1 = Frame(self, bd=4, relief=RIDGE, bg="#D9D9D9")
        table1.place(y=50, width=290, height=450)

        name_document= Label(table1, text="DOKUMEN", bg="#D9D9D9", font=("cambria", 20, "bold"))
        name_document.grid(row=0, columnspan=2, pady=5, padx=75)

        #LABEL 1
        label_name = Label(table1, text="Nama ", bg="#D9D9D9", font=("cambria", 12))
        label_name.grid(row=1,column=0, pady=10, padx=10, sticky="w")
        label_nim = Label(table1, text="NIM ", bg="#D9D9D9", font=("cambria", 12))
        label_nim.grid(row=2,column=0, pady=10, padx=10, sticky="w")
        label_prodi = Label(table1, text="Prodi", bg="#D9D9D9", font=("cambria", 12))
        label_prodi.grid(row=3,column=0, pady=10, padx=10, sticky="w")
        label_umur = Label(table1, text="Umur",bg="green",font=("cambria", 12))
        label_umur.grid(row=4,colum=0,pady=10, padx=10, sticky="w")
        label_agama = Label(table1, text="Agama",bg="green",font=("cambria", 12))
        label_agama.grid(row=5,colum=0,pady=10, padx=10, sticky="w")
        label_nohp= Label(table1, text="NOHP",bg="green",font=("cambria", 12))
        label_nohp.grid(row=6,colum=0,pady=10, padx=10, sticky="w")

        self.entry_name = Entry(table1,textvariable=self.var_name, bd=3, relief=GROOVE, width=30)
        self.entry_name.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        self.entry_nim = Entry(table1,textvariable=self.var_nim, bd=3, relief=GROOVE, width=30)
        self.entry_nim.grid(row=2, column=1, pady=10, padx=10, sticky="w")
        self.entry_prodi = Entry(table1,textvariable=self.var_prodi, bd=3, relief=GROOVE, width=30)
        self.entry_prodi.grid(row=3, column=1, pady=10, padx=10, sticky="w")
        self.entry_umur = Entry(table1,textvariable=self.var_prodi, bd=3, relief=GROOVE, width=30)
        self.entry_umur.grid(row=4, column=1, pady=10, padx=10, sticky="w")
        self.entry_agama = Entry(table1,textvariable=self.var_prodi, bd=3, relief=GROOVE, width=30)
        self.entry_agama.grid(row=5, column=1, pady=10, padx=10, sticky="w")
        self.entry_nohp = Entry(table1,textvariable=self.var_prodi, bd=3, relief=GROOVE, width=30)
        self.entry_nohp.grid(row=6, column=1, pady=10, padx=10, sticky="w")

        self.label = Label(table1, text = "", bg="#D9D9D9")
        self.label.place(x =10, y=300) 
        #========================================

        #TABEL 2
        table2 = Frame(self, bd=4, relief=RIDGE, bg="white")
        table2.place(y=50, x=300, width=719, height=450)
        
        #SCROLL
        scroll_x= Scrollbar(table2, orient=HORIZONTAL)
        scroll_y= Scrollbar(table2, orient=VERTICAL)  
        self.document_table = ttk.Treeview(table2, column=("Nama", "NIM", "Prodi", "Umur", "Agama", "NOHP", "File"), xscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)    
        scroll_y.config(command=self.document_table.yview)
        scroll_x.config(command=self.document_table.xview)
        #=================================

        #TABEL 3  
        table3 = Frame(self, bd=4, relief=RIDGE, bg="#D9D9D9")
        table3.place(y=410, x=10, width=268, height=55)

        #ADD, CLEAR, EDIT, SAVE
        self.filepath="" #Mempertahankan File ketika melakukan Edit
        addbtn = Button(table3, text="Tambah", command=self.add_document, width="9", bg="#A1A5A6").grid(row=0,column=0, padx=7, pady=10)
        editbtn = Button(table3, text="Edit", command=self.edit_data, width="9", bg="#A1A5A6").grid(row=0,column=1, padx=7, pady=10) 
        clearbtn = Button(table3, text="Bersihkan", command=self.clear, width="9", bg="#A1A5A6").grid(row=0,column=3, padx=7, pady=10)

        #MENU TAMBAH FILE
        self.addfilebtn = Button(table1, text="Add File", command=self.openfile, width="9", bg="#A1A5A6")
        self.addfilebtn.place(x=110,y=260)
        #====================================

        #ISI TABEL
        self.document_table.heading("Nama", text="Nama")
        self.document_table.heading("NIM", text="NIM")
        self.document_table.heading("Prodi", text="Prodi")
        self.document_table.heading("Umur", text="Umur")
        self.document_table.heading("Agama", text="Agama")
        self.document_table.heading("NO HP", text="NO HP")
        self.document_table.heading("File", text="File")
        self.document_table["show"]="headings"
        self.document_table.column("Nama", width=100)
        self.document_table.column("NIM", width=100)
        self.document_table.column("Prodi", width=100)
        self.document_table.column("Umur", width=100)
        self.document_table.column("Agama", width=100)
        self.document_table.column("NOHP", width=100) 
        self.document_table.column("File", width=100)
        self.document_table.pack(fill=BOTH, expand=1)
        self.document_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_data()



class proses_data():
    #PROGRAM PROSES DATA
    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
            string_path = os.path.split(filename)
        return binaryData, string_path[1]


    def insertBLOB(self, nama, nim, prodi, umur, agama, nohp, digitalFile=None):
        print("Inserting BLOB into document table")
        con, cur = self.connect_start()
        sql_insert_blob_query = """ INSERT INTO document
        (nama, nim, prodi, umur, agama, nohp, filename, file) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,)"""
        print(digitalFile)
        if digitalFile != None :
            binaryFile, string_path = self.convertToBinaryData(digitalFile)
        else :
            binaryFile=""
            string_path=""

        insert_blob_tuple = (nama, nim, prodi, umur, agama, nohp, string_path, binaryFile)
        result = cur.execute(sql_insert_blob_query, insert_blob_tuple)
        print("File inserted successfully as a BLOB into document table", result)
        self.connect_end(con,cur)
        print("MySQL connection is closed")


    def write_file(self, data, filename):
        # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)


    def readBLOB(self, nim, digitalFile):
        print("Reading BLOB data from document table")
        con, cur = self.connect_start()
        sql_fetch_blob_query = """SELECT * from document where nim = %s"""
        cur.execute(sql_fetch_blob_query, (nim,))
        record = cur.fetchall()
        for row in record:
            print("nama = ", row[0], )
            print("nim = ", row[1], )
            print("prodi = ", row[2] )
            print("umur = ", row[3], )
            print("agama = ", row[4], )
            print("nohp = ", row[5], )
            file = row[6]
            print("Storing file mahasiswa on disk \n")
            self.write_file(file, digitalFile)
        self.connect_end(con,cur)
        print("MySQL connection is closed")


    def prosesedit(self, nama, nim, prodi, umur, agama, nohp, digitalFile):
        con, cur = self.connect_start()
        if (digitalFile == ""):
            sql_check_query = """SELECT * from document where nim = %s"""
            cur.execute(sql_check_query, (nim,))
            record = cur.fetchall()
            for row in record:
                check_nama = row[0]
                check_prodi = row[2]
                check_umur = row[3]
                check_agama = agama[4]
                check_nohp = nohp[5]
            if (check_nama == nama and check_prodi == prodi or check_umur == umur and check_nohp == nohp and check_agama == agama ):
                print("No Updated")
            else :
                sql_update_query = """UPDATE document set nama = %s, prodi = %s,umur = %s, agama = %s, nohp = %s, where nim = %s"""
                input_data = (nama, prodi,umur, agama, nohp, nim)
                cur.execute(sql_update_query, input_data)
                print("Record NIM =",(nim),"Updated successfully")

        else :
            sql_update_query = """UPDATE document set nama = %s, prodi = %s, umur = %s, agama = %s, nohp = %s, filename = %s, file = %s where nim = %s"""
            binaryFile, string_path = self.convertToBinaryData(digitalFile)
            input_data = (nama, prodi,umur, agama, nohp, string_path, binaryFile, nim)
            cur.execute(sql_update_query, input_data)
            print("Record NIM =",(nim),"Updated successfully")
        self.connect_end(con,cur)
    #--------------------------------------------------



class program(document, proses_data):
    def __init__(self, root, controller):
        super().__init__(root, controller)

    #PROGRAM AKSES DATA
    def openfile(self):
        self.filepath = filedialog.askopenfilename(initialdir="D:/Kuliah", filetypes=(("all files", "*.*"),("png files", "*.png"),
                                                                            ("jpg files", "*.jpg"), ("pdf files", "*.pdf"),
                                                                            ("docx files","*docx")))
        if (self.filepath!=""):
            self.label.configure(text = self.filepath, bg="yellow")
            print('Selected:',self.filepath)
    

    def add_document(self):
        self.insertBLOB (self.var_name.get(),self.var_nim.get(),self.var_prodi.get(),self.var_umur.get(),self.var_agama.get(),self.var_nohp.get(),self.filepath)


    def download(self):
        con, cur = self.connect_start()
        sql_check_query = """SELECT filename from document where nim = %s"""
        cur.execute(sql_check_query, (self.var_nim.get()))
        record = cur.fetchall()
        for row in record :
            filename = row[0]
        con.commit()
        cur.close()
        con.close()
        self.filesave = filedialog.asksaveasfilename(initialdir="D:/", initialfile=filename, 
                                                    filetypes=(("all files", "*.*"),("png files", "*.png"),
                                                                ("jpg files", "*.jpg"), ("pdf files", "*.pdf"),
                                                                ("docx files","*docx")))
        myfile=open(self.filesave, "w+")
        self.readBLOB (self.var_nim.get(), self.filesave)


    def edit_data(self):
        self.prosesedit (self.var_name.get(),self.var_nim.get(),self.var_prodi.get(),self.var_umur.get(),self.var_agama.get(),self.var_nohp.get(),self.filepath)


    def delete_data(self):
        con, cur = self.connect_start()
        cur.execute("DELETE from document where nim=%s", self.var_nim.get())
        self.connect_end(con,cur)
    

    def search_data(self):
        con, cur = self.connect_start()
        cur.execute("SELECT * from document where nama LIKE '%"+str(self.var_search.get())+"%'" 
                                                    "or nim LIKE '%"+str(self.var_search.get())+"%'"
                                                    "or prodi LIKE '%"+str(self.var_search.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.document_table.delete(*self.document_table.get_children())
            for row in rows:
                data = list(row)
                if (data[3]==""):
                    data[3]= str("File Tidak Tersedia")
                self.document_table.insert("", END, values=data)
            con.commit()
        con.close()


    def show_data(self):
        con, cur = self.connect_start()
        cur.execute("SELECT * from document")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.document_table.delete(*self.document_table.get_children())
            for row in rows:
                data = list(row)
                if (data[3]==""):
                    data[3]= str("File Tidak Tersedia")
                self.document_table.insert("", END, values=data)
            con.commit()
        con.close()


    def clear(self):
        self.var_name.set(""),
        self.var_nim.set(""),
        self.var_prodi.set(""),
        self.var_umur.set(""),
        self.var_agama.set(""),
        self.var_nohp.set(""),
        self.label.configure(text = "", bg="#D9D9D9")
        self.entry_nim.config(state="normal")
        self.filepath=""


    def get_cursor(self, ev):
        cursor_row=self.document_table.focus()
        content=self.document_table.item(cursor_row)
        row=content["values"]
        self.var_name.set(row[0])
        self.entry_nim.config(state="disabled")
        self.var_nim.set(row[1])
        self.var_prodi.set(row[2])
        self.var_umur.set(row[3])
        self.var_agama.set(row[4])
        self.var_nohp.set(row[5])
        

    def connect_start(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="document")
        cur=con.cursor()
        return con, cur


    def connect_end(self, con,cur):
        con.commit()
        cur.close()
        con.close()
        self.show_data()
        self.clear()


    #MENU KELUAR
    #def close(self, event=None):
        #if mb.askyesno('Konfirmasi', 'Keluar dari program?', parent=self.root):
            #self.root.destroy()
    #====================================    


#OUTPUT
if __name__ == '__main__':
    app = MyApp()
    app.title('Document Managment System')
    app.geometry("1020x540")
    app.resizable(False, False)
    app.mainloop()
