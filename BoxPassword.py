class App:
    def __init__(self, master):
        #Frame for Button
        self.FraBut = Frame(master)
        self.FraBut.place(x=80, y=100)
        #Button creat and inout
        self.ButCreatRec = Button(self.FraBut, text='CREAT', height=1, width=15, font = ('Times', 10, 'bold'), command=self.create_akk, fg='white', bg='#81d4fa')
        self.ButCreatRec.pack()

        self.ButInRec = Button(self.FraBut, text='INOUT', height=1, width=15, font = ('Times', 10, 'bold'), command=self.inout_akk, fg='white', bg='#81d4fa')
        self.ButInRec.pack()
        #Field login and passwd
        self.LogEnt = Entry(master, width=40, font = ('Times', 10))
        self.LogEnt.place(x=10, y=35)
        self.PasEnt = Entry(master, width=40, font = ('Times', 10), show='*')
        self.PasEnt.place(x=10, y=75)

        self.text_log = Label(master, text='Login', bg='#ffccbc')
        self.text_log.place(x=10, y=10)

        self.text_pas = Label(master, text='Password', bg='#ffccbc')
        self.text_pas.place(x=10, y=54)

    #func creat akk
    def create_akk(self):
        login_cr = self.LogEnt.get() #field login
        password_cr = self.PasEnt.get() #field password
        len_login = len(login_cr)   #for check log
        len_password = len(password_cr) #for check pas
        datarec = (login_cr, password_cr) #collection in one
        for_creat_db = login_cr + password_cr
        check_valid = []
        if len_login > 0 and len_password > 0:
            bas = sqlite3.connect('lp.db')
            in_rec = bas.cursor()
            in_rec.execute("CREATE TABLE IF NOT EXISTS datalp(login, password);") #create table
            for row in in_rec.execute('SELECT * FROM datalp'): #validation chek login....
                check_valid.append(row[0])
            if login_cr not in check_valid:
                in_rec.execute("INSERT INTO datalp VALUES(?, ?);", datarec) #insert values
                bas.commit()
                self.clear_ent()
                self.createBDmain(for_creat_db) #func create db main for users
            else:
                self.clear_ent() #....validation chek login
        else:
            self.clear_ent()

    #func create db main for users  
    def createBDmain(self, namecreat):
        bas = sqlite3.connect(namecreat + '.db')
        in_rec = bas.cursor()
        in_rec.execute("CREATE TABLE IF NOT EXISTS datausers(account, login, password, link, notes);")
        bas.commit()

    #func inout akk
    def inout_akk(self):
        login_in = self.LogEnt.get() #field login
        password_in = self.PasEnt.get() #field passwd
        len_login = len(login_in) #for chek log
        len_password = len(password_in) #for chek pass
        check_login = []
        check_password = []
        login_del = login_in
        password_del = password_in
        for_ShowDB = login_in + password_in
        if len_login > 0 and len_password > 0:
            bas = sqlite3.connect('lp.db')
            in_rec = bas.cursor()
            for row in in_rec.execute('SELECT * FROM datalp'):
                check_login.append(row[0])
                check_password.append(row[1])
            if login_in not in check_login:
                self.LogEnt.delete(0, END)
            if password_in not in check_password:
                self.PasEnt.delete(0, END)
            else:
                self.clear_ent()
                self.show_db(for_ShowDB, login_del, password_del)

        else:
            self.clear_ent()

    #Func clear field log and pas
    def clear_ent(self):
        self.LogEnt.delete(0, END)
        self.PasEnt.delete(0, END)

     #func show user db       
    def show_db(self, for_showDB, login_delete, password_delete):
        self.for_showDB = for_showDB #login+password
        win = Tk()
        win.geometry('550x450')
        win.resizable(width=False, height=False)
        win['bg'] = '#ffccbc'

        #func for settings
        def edit_rec(*args):
            setings_edit = Tk()
            setings_edit.geometry('300x200')
            setings_edit.resizable(width=False, height=False)
            setings_edit['bg'] = '#ffccbc'

            edit_account = Entry(setings_edit, width=30)
            edit_account.place(x=10, y=10)
            textE_acc = Label(setings_edit, text='Account', bg='#ffccbc')
            textE_acc.place(x=210, y=5)

            edit_login = Entry(setings_edit, width=30)
            edit_login.place(x=10, y=40)
            textE_log = Label(setings_edit, text='Login', bg='#ffccbc')
            textE_log.place(x=210, y=40)

            edit_password = Entry(setings_edit, width=30)
            edit_password.place(x=10, y=70)
            textE_pas = Label(setings_edit, text='Password', bg='#ffccbc')
            textE_pas.place(x=210, y=70)

            edit_link = Entry(setings_edit, width=30)
            edit_link.place(x=10, y=100)
            textE_link = Label(setings_edit, text='Link', bg='#ffccbc')
            textE_link.place(x=210, y=100)

            edit_notes = Entry(setings_edit, width=30)
            edit_notes.place(x=10, y=130)
            textE_note = Label(setings_edit, text='Note', bg='#ffccbc')
            textE_note.place(x=210, y=130)

            #func write in db
            def write_db(*args):
                account = edit_account.get()
                login = edit_login.get()
                password = edit_password.get()
                link = edit_link.get()
                notes = edit_notes.get()
                datarec = (account, login, password, link, notes)
                com = sqlite3.connect(for_showDB + '.db')
                rec = com.cursor()
                rec.execute("INSERT INTO datausers VALUES(?, ?, ?, ?, ?)", datarec)
                com.commit()
                edit_account.delete(0, END)
                edit_login.delete(0, END)
                edit_password.delete(0, END)
                edit_link.delete(0, END)
                edit_notes.delete(0, END)

            #func delete values
            def del_values(*args):
                account = edit_account.get()
                com = sqlite3.connect(for_showDB + '.db')
                rec = com.cursor()
                rec.execute("DELETE FROM datausers WHERE account='{name}'".format(name=account))
                com.commit()
                edit_account.delete(0, END)
                edit_login.delete(0, END)
                edit_password.delete(0, END)
                edit_link.delete(0, END)
                edit_notes.delete(0, END)
                showent_login.delete(0, END)
                showent_password.delete(0, END)
                showent_link.delete(0, END)
                showent_note.delete(0, END)
                get_val_ent.delete(0, END)

            #finc delete account
            def del_account(*args):
                com = sqlite3.connect('lp.db')
                rec = com.cursor()
                rec.execute("DELETE FROM datalp WHERE login='{name}' and password='{name_2}'".format(name=login_delete, name_2=password_delete))
                com.commit()
                remove(for_showDB + '.db')
                edit_account.delete(0, END)
                edit_login.delete(0, END)
                edit_password.delete(0, END)
                edit_link.delete(0, END)
                edit_notes.delete(0, END)
                showent_login.delete(0, END)
                showent_password.delete(0, END)
                showent_link.delete(0, END)
                showent_note.delete(0, END)
                get_val_ent.delete(0, END)
                
            write_but = Button(setings_edit, text='WRITE', command=write_db, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
            write_but.place(x=10, y=160)

            del_but = Button(setings_edit, text='DEL', command=del_values, fg='#ff6d00', bg='#81d4fa', font = ('Times', 10, 'bold'))
            del_but.place(x=70, y=160)

            delacc_but = Button(setings_edit, text='DEL ACCOUNT', command=del_account, fg='#ef5350', bg='#81d4fa', font = ('Times', 10, 'bold'))
            delacc_but.place(x=200, y=160)

            setings_edit.mainloop()

        #func get in entry values
        def get_values(*args):
            get_val_f = get_val_ent.get()
            com = sqlite3.connect(for_showDB + '.db')
            rec = com.cursor()
            rec.execute('SELECT * FROM datausers WHERE account="{name}"'.format(name=get_val_f))
            rows = rec.fetchall()
            for log in rows:
                showent_login.delete(0, END)
                showent_login.insert(END, log[1])
                showent_password.delete(0, END)
                showent_password.insert(0, log[2])
                showent_link.delete(0, END)
                showent_link.insert(0, log[3])
                showent_note.delete(0, END)
                showent_note.insert(0, log[4])

        label_show = Label(win, width=25, height=25, bg='#ffccbc')
        label_show.place(x=10, y=20)
        
        #Block field get values
        get_val_lab = Label(win, bg='#f5f5f5')
        get_val_lab.place(x=200, y=80)
        get_val_ent = Entry(get_val_lab, width=30)
        get_val_ent.grid(row=0, column=0)
        get_but = Button(get_val_lab, text='GET', height=1, width=10, command=get_values, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        get_but.grid(row=0, column=1)
        text_acc = Label(win, text='Account', bg='#ffccbc')
        text_acc.place(x=200, y=50)
        

        #func clear entrys
        def clear_entry(*args):
            get_val_ent.delete(0, END)
            showent_login.delete(0, END)
            showent_password.delete(0, END)
            showent_link.delete(0, END)
            showent_note.delete(0, END)

        #Block for left Listbox
        scrollbar = Scrollbar(label_show)
        scrollbar.pack(side=LEFT, fill=Y)
        show_rec = Listbox(label_show, width=25, height=25, yscrollcommand=scrollbar.set, font = ('Times', 9, 'bold'))
        show_rec.pack()
        scrollbar.config(command=show_rec.yview)

        #show accounts Listbox
        def showDBvalues(*args):
            show_rec.delete(0, END)
            com = sqlite3.connect(for_showDB + '.db')
            rec = com.cursor()
            mas_acc = []
            for item in rec.execute('SELECT * FROM datausers'):
                mas_acc.append(item[0])
            mas_acc.reverse()
            for sh in mas_acc:
                show_rec.insert(0, sh)
        showDBvalues()

        #Block copy entry values
        def copyin_login(*args):
            cop_log = showent_login.get()
            copy(cop_log)

        def copyin_password(*args):
            cop_pas = showent_password.get()
            copy(cop_pas)

        def copyin_link(*args):
            cop_lin = showent_link.get()
            copy(cop_lin)

        def copyin_note(*args):
            cop_note = showent_note.get()
            copy(cop_note)

        #Button for update for shoeDBvalues
        update_showDBvalues = Button(win, text='UPDATE', height=1, width=10, command=showDBvalues, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        update_showDBvalues.place(x=200, y=10)

        #Block for login
        showlab_login = Label(win, height=25, width=55, bg='#ffccbc')
        showlab_login.place(x=200, y=160)
        showent_login = Entry(showlab_login, width=45)
        showent_login.grid(row=0, column=0)
        inshowentL = Label(showlab_login, bg='#ffccbc')
        inshowentL.grid(row=1, column=0)
        copy_login = Button(inshowentL, text='COPY', height=1, width=5, command=copyin_login, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        copy_login.grid(row=0, column=1)
        text_log = Label(win, text='Login', bg='#ffccbc')
        text_log.place(x=200, y=130)

        #Block for password
        showlab_password = Label(win, height=25, width=55, bg='#ffccbc')
        showlab_password.place(x=200, y=230)
        showent_password = Entry(showlab_password, width=45)
        showent_password.grid(row=0, column=0)
        inshowentP = Label(showlab_password, bg='#ffccbc')
        inshowentP.grid(row=1, column=0)
        copy_password = Button(inshowentP, text='COPY', height=1, width=5, command=copyin_password, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        copy_password.grid(row=0, column=1)
        text_pas = Label(win, text='Password', bg='#ffccbc')
        text_pas.place(x=200, y=200)


        #Block for link
        showlab_link = Label(win, height=25, width=55, bg='#ffccbc')
        showlab_link.place(x=200, y=300)
        showent_link = Entry(showlab_link, width=45)
        showent_link.grid(row=0, column=0)
        inshowentL = Label(showlab_link, bg='#ffccbc')
        inshowentL.grid(row=1, column=0)
        copy_link = Button(inshowentL, text='COPY', height=1, width=5, command=copyin_link, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        copy_link.grid(row=0, column=1)
        text_link = Label(win, text='Link', bg='#ffccbc')
        text_link.place(x=200, y=270)

        #Block for note
        showlab_note = Label(win, height=25, width=55, bg='#ffccbc')
        showlab_note.place(x=200, y=370)
        showent_note = Entry(showlab_note, width=45)
        showent_note.grid(row=0, column=0)
        inshowentN = Label(showlab_note, bg='#ffccbc')
        inshowentN.grid(row=1, column=0)
        copy_note = Button(inshowentN, text='COPY', height=1, width=5, command=copyin_note, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        copy_note.grid(row=0, column=1)
        text_acc = Label(win, text='Note', bg='#ffccbc')
        text_acc.place(x=200, y=340)

        #Button settings
        settings_but = Button(win, text='EDITING', height=1, width=10, command=edit_rec, fg='#ff6d00', bg='#81d4fa', font = ('Times', 10, 'bold'))
        settings_but.place(x=400, y=10)

        #Button clear
        clear_but = Button(win, text='CLEAR', height=1, width=10, command=clear_entry, fg='white', bg='#81d4fa', font = ('Times', 10, 'bold'))
        clear_but.place(x=300, y=10)

        win.mainloop()

if __name__ == '__main__':
    import sqlite3
    from tkinter import *
    from os import remove
    from pyperclip import copy
    root = Tk()
    root.geometry('270x160')
    root.resizable(width=False, height=False)
    root['bg'] = '#ffccbc'
    root.title('')
    app = App(root)
    root.mainloop()       