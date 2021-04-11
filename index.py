import mysql.connector
import tkinter as tk

def main(cursor):
    root = tk.Tk()
    root.title("SMART DOCTOR")
    root.geometry("500x500")
    
    tk.Label(root, text="SMART DOCTOR",font=('calibre',20, 'bold')).grid(row=0)
    tk.Button(root, text='Login', command=lambda: Login(cursor,root)).grid(row=1, column=0)
    tk.Button(root, text='Register', command=lambda: Register(cursor,root)).grid(row=2, column=0)
    tk.Button(root, text='Exit', command=lambda: Exit(root)).grid(row=3, column=0)
    root.mainloop()

def Login_main(cursor):
    root = tk.Tk()
    root.title("SMART DOCTOR")
    root.geometry("500x500")
    
    tk.Label(root, text="Logged In",font=('calibre',20, 'bold')).grid(row=0)
    tk.Button(root, text='View', command=lambda: View(cursor,root)).grid(row=1, column=0)
    tk.Button(root, text='Chat Bot', command=lambda: Chatbox(cursor,root)).grid(row=2, column=0)
    tk.Button(root, text='Log Out', command=lambda: close_main(cursor,root)).grid(row=3, column=0)
    root.mainloop()
        
def View(cursor,root):
    root.destroy()

    def Doctor_Name(cursor,root):
        root.destroy()

        def Submit():
            name=name_var.get()
            sql = "SELECT * FROM doctors WHERE Name LIKE '%"+name+"%'"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result)>0:
                for x in result:
                    print(x)
            else:
                print("No results matching your search")
            root.destroy()
            Login_main(cursor)
    
        root = tk.Tk()
        root.title("SMART DOCTOR")
        root.geometry("500x500")
        
        name_var=tk.StringVar()
    
        tk.Label(root, text="Doctor Name :",font=('calibre',20, 'bold')).grid(row=0)
        tk.Label(root, text = 'Doctor Name', font=('calibre',10, 'bold')).grid(row=1, column=0)
        tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')).grid(row=1, column=1)
        tk.Button(root,text = 'Filter', command = Submit).grid(row=3, column=1)
        root.mainloop()
    
    def Doctor_Hospital(cursor,root):
        root.destroy()
        
        def Submit():
            hospital=hosp_var.get()
            sql = "SELECT * FROM doctors WHERE Hospital LIKE '%"+hospital+"%'"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result)>0:
                for x in result:
                    print(x)
            else:
                print("No results matching your search")
            root.destroy()
            Login_main(cursor)
    
        root = tk.Tk()
        root.title("SMART DOCTOR")
        root.geometry("500x500")
        
        hosp_var=tk.StringVar()
    
        tk.Label(root, text="Doctor Hospital :",font=('calibre',20, 'bold')).grid(row=0)
        tk.Label(root, text = 'Doctor Hospital', font=('calibre',10, 'bold')).grid(row=1, column=0)
        tk.Entry(root,textvariable = hosp_var, font=('calibre',10,'normal')).grid(row=1, column=1)
        tk.Button(root,text = 'Filter', command = Submit).grid(row=3, column=1)
        root.mainloop()
    
    def Doctor_Specialization(cursor,root):
        root.destroy()

        def Submit():
            specialization=spec_var.get()
            sql = "SELECT * FROM doctors WHERE Specialization LIKE '%"+specialization+"%'"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result)>0:
                for x in result:
                    print(x)
            else:
                print("No results matching your search")
            root.destroy()
            Login_main(cursor)
    
        root = tk.Tk()
        root.title("SMART DOCTOR")
        root.geometry("500x500")
        
        spec_var=tk.StringVar()
    
        tk.Label(root, text="Doctor Specialization :",font=('calibre',20, 'bold')).grid(row=0)
        tk.Label(root, text = 'Doctor Specialization', font=('calibre',10, 'bold')).grid(row=1, column=0)
        tk.Entry(root,textvariable = spec_var, font=('calibre',10,'normal')).grid(row=1, column=1)
        tk.Button(root,text = 'Filter', command = Submit).grid(row=3, column=1)
        root.mainloop()

    root = tk.Tk()
    root.title("SMART DOCTOR")
    root.geometry("500x500")
    
    tk.Label(root, text="Filter By",font=('calibre',20, 'bold')).grid(row=0)
    tk.Button(root, text='Doctor Name', command=lambda: Doctor_Name(cursor,root)).grid(row=1, column=0)
    tk.Button(root, text='Doctor Hospital', command=lambda: Doctor_Hospital(cursor,root)).grid(row=2, column=0)
    tk.Button(root, text='Doctor Specialization', command=lambda: Doctor_Specialization(cursor,root)).grid(row=3, column=0)
    root.mainloop()

def Chatbox(cursor,root):
    root.destroy()

    def Submit():
        string=string_var.get()
        f = open("chatbot.txt", "r")
        flag=0
        for x in f:
            if flag:
                print(x)
                break
            if x.strip().find(string.lower())!=-1:
                flag=1
        if not flag:
            print("Sorry I was unable the question :(")
        f.close()
        root.destroy()
        Login_main(cursor)

    root = tk.Tk()
    root.title("SMART DOCTOR")
    root.geometry("500x500")
    
    string_var=tk.StringVar()

    tk.Label(root, text="Let me clear your doubts...",font=('calibre',20, 'bold')).grid(row=0)
    tk.Entry(root,textvariable = string_var, font=('calibre',10,'normal')).grid(row=1, column=0)
    tk.Button(root,text = 'Go', command = Submit).grid(row=2, column=0)
    root.mainloop()

def Login(cursor,root):
    root.destroy()

    def Submit():
        name=name_var.get()
        password=passw_var.get()
        sql = "SELECT * FROM doctors WHERE Name = %s AND Password = %s"
        val = (name,password, )
        cursor.execute(sql,val)
        result = cursor.fetchall()
        if len(result)>0:
            print("Logged in")
            root.destroy()
            Login_main(cursor)
        else:
            print("Invalid Entry")
        name_var.set("")
        passw_var.set("")
        root.destroy()
        main(cursor)
 
    root = tk.Tk()
    root.title("SMART DOCTOR")
    root.geometry("500x500")
    
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    
    tk.Label(root, text="Login :",font=('calibre',20, 'bold')).grid(row=0)
    tk.Label(root, text = 'Username', font=('calibre',10, 'bold')).grid(row=1, column=0)
    tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')).grid(row=1, column=1)
    tk.Label(root, text = 'Password', font=('calibre',10, 'bold')).grid(row=2, column=0)
    tk.Entry(root,textvariable = passw_var, font=('calibre',10,'normal')).grid(row=2, column=1)
    tk.Button(root,text = 'Submit', command = Submit).grid(row=3, column=1)
    root.mainloop()

def Register(cursor,root):
    root.destroy()
    
    def Submit():
        name=name_var.get()
        password=passw_var.get()
        hospital=hosp_var.get()
        specialization=spec_var.get()
        sql = "INSERT INTO doctors (Name,Password,Hospital,Specialization) VALUES (%s,%s,%s,%s)"
        val = (name,password,hospital,specialization)
        cursor.execute(sql, val)
        db.commit()
        print(cursor.rowcount, "record successfully inserted")
        root.destroy()
        main(cursor)

    root = tk.Tk()
    root.title("SMART DOCTOR")
    root.geometry("500x500")
    
    name_var=tk.StringVar()
    passw_var=tk.StringVar()
    hosp_var=tk.StringVar()
    spec_var=tk.StringVar()
    
    tk.Label(root, text="Register",font=('calibre',20, 'bold')).grid(row=0)
    tk.Label(root, text = 'Name', font=('calibre',10, 'bold')).grid(row=1, column=0)
    tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal')).grid(row=1, column=1)
    tk.Label(root, text = 'Password', font=('calibre',10, 'bold')).grid(row=2, column=0)
    tk.Entry(root,textvariable = passw_var, font=('calibre',10,'normal')).grid(row=2, column=1)
    tk.Label(root, text = 'Hospital Name', font=('calibre',10, 'bold')).grid(row=3, column=0)
    tk.Entry(root,textvariable = hosp_var, font=('calibre',10,'normal')).grid(row=3, column=1)
    tk.Label(root, text = 'Specialization', font=('calibre',10, 'bold')).grid(row=4, column=0)
    tk.Entry(root,textvariable = spec_var, font=('calibre',10,'normal')).grid(row=4, column=1)
    tk.Button(root,text = 'Submit', command = Submit).grid(row=5, column=1)
    root.mainloop()

def Exit(root):
    root.destroy()
    print("Thank You")
    exit() 

def close_main(cursor,root):
    root.destroy()
    main(cursor)
    
if __name__=="__main__":
    db = mysql.connector.connect(
    host="localhost",
    user="Daniel Davidraj",
    password="password",
    database="hospital"
    )
    cursor = db.cursor()
    main(cursor)
    #print(db)


    
