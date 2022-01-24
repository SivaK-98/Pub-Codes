from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = Tk()

# app title
root.title("Vault")

# window size
root.maxsize(width=500 ,  height=500)
root.minsize(width=500 ,  height=500)


def login():
    pass


def clear():
    pass
#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
    con = sqlite3.connect('/home/siva/Documents/Siva/Code/python/Tkinter-App/vault.db')
    cursor = con.cursor()
    count = cursor.execute('select count(*) from user;').fetchall()
    num_of_rows = count[0][0]
    print(num_of_rows)

	# signup database connect 
    def action():
        db_count = cursor.execute("select count(*) from user;").fetchone()[0]
        id = db_count
        if name.get()=="" or email.get()==""or username.get()=="" or password.get()=="" or very_pass.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
        else:
            try:
                con = sqlite3.connect('/home/siva/Documents/Siva/Code/python/Tkinter-App/vault.db')
                cur = con.cursor()
                param1 = (username.get())
                query1 = "select * from user where username=?"
                cur.execute(query1,list(param1))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                else:
                    db_count = cursor.execute("select count(*) from user;").fetchone()[0]
                    id = db_count
                    query = """INSERT INTO user(id, name, email, username, password,) VALUES (?, ?, ?, ?, ?,);"""
                    params = (id,name.get(),email.get(),username.get(),password.get(),)
                    #params = list(params)
                    print(params)
                    cur.execute(query, params)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
                    clear()
                    switch()
            except Exception as es:
                messagebox.showerror("Error" , f"Error Due to : {str(es)}", parent = winsignup)
                print(es)

	# close signup function			
    def switch():
        winsignup.destroy()

	# clear data function
    def clear():
        name.delete(0,END)
        email.delete(0,END)
        username.delete(0,END)
        password.delete(0,END)
        very_pass.delete(0,END)


	# start Signup Window	
    winsignup = Tk()
    winsignup.title("Docter Appointment App")
    winsignup.maxsize(width=500 ,  height=600)
    winsignup.minsize(width=500 ,  height=600)


	#heading label
    heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
    heading.place(x=80 , y=60)

	# form data label
    Name = Label(winsignup, text= "Name :" , font='Verdana 10 bold')
    Name.place(x=40,y=130)
    
    Email = Label(winsignup, text= "Email :" , font='Verdana 10 bold')
    Email.place(x=40,y=160)
    
    username = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
    username.place(x=40,y=190)
    
    password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
    password.place(x=40,y=220)
    
    very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
    very_pass.place(x=40,y=250)

	# Entry Box ------------------------------------------------------------------
    name = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()
    very_pass = StringVar()
    
    name = Entry(winsignup, width=40 , textvariable = name)
    name.place(x=200 , y=133)
    
    email = Entry(winsignup, width=40 , textvariable = email)
    email.place(x=200 , y=163)
    
    username = Entry(winsignup, width=40,textvariable = username)
    username.place(x=200 , y=193)
    
    password = Entry(winsignup, width=40, show="*" ,textvariable = password)
    password.place(x=200 , y=223)
    
    very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
    very_pass.place(x=200 , y=253)


	# button login and clear
    
    btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
    btn_signup.place(x=200, y=413)
    
    btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
    btn_login.place(x=280, y=413)
    
    sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
    sign_up_btn.place(x=350 , y =20)
    
    winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------


# Main Page Login Window
heading = Label(root , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = Label(root, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(root, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

username = StringVar()
password = StringVar()
	
userentry = Entry(root, width=40 , textvariable = username)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(root, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)

# button login and clear

btn_login = Button(root, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(root, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(root , text="Switch To Sign up" , command = signup )
sign_up_btn.place(x=350 , y =20)


root.mainloop()



