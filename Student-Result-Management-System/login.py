#Login System
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import sqlite3
import os
class Login:
    def __init__(self, home):
        self.home=home
        self.home.title("Login System")
        self.home.geometry("1600x900+0+0")
        #====BG IMage=====
        #self.bg=ImageTk.PhotoImage(file="images/6.jpg")
        #self.bg_image=Label(self.home,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.home,bg="white")
        Frame_login.place(x=580,y=100,height=550,width=500)

        # Login title
        title=Label(Frame_login,text="User Login",font=("Times New Roman",25,"bold"),fg="navy blue",bg="light gray").place(x=150,y=20)

        #Username and password lable
        lbl_user=Label(Frame_login,text="User Name",font=("Times New Roman",15,"bold"),fg="black",bg="light gray").place(x=45,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_user.place(x=45,y=170,width=400,height=35)


        lbl_pass=Label(Frame_login,text="Password",font=("Times New Roman",15,"bold"),fg="black",bg="light gray").place(x=45,y=240)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.txt_pass.place(x=45,y=270,width=400,height=35)

        #Buttons
        login=Button(Frame_login,command=self.login_function,text="Login",cursor="hand2",bg="navy blue",fg="white",font=("times new roman",20,"bold")).place(x=210,y=370,width=100,height=50)



#Function for Login Part   
    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error","All fields are requires",parent=self.home)
        
        elif self.txt_pass.get() == "1234" or self.txt_user.get() == "admin":
            messagebox.showinfo("Success", f"Welcome :- {self.txt_user.get()}", parent=self.home)
            self.home.destroy()
            os.system("python dashboard.py")

        else:
            messagebox.showerror("Error", "Wrong Username or Password", parent=self.home)


home = Tk()
obj = Login(home)
home.mainloop()
