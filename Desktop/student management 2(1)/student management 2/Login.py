from tkinter import* 
from PIL import ImageTk
from tkinter import messagebox
import os
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Form")
        self.root.geometry("1520x785+0+0")
        
        #===========Image============#
        self.bg=ImageTk.PhotoImage(file="th.jpeg")
        self.bg_image=Label(self.root,image=self.bg).place(x=10,y=130,width=1250,height=470)
        
        #============Login Frame===================#
        Frame_login=Frame(self.root,bg="#DEE4E7")
        Frame_login.place(x=450,y=120,height=450,width=450)
        
        #================Title And Description==========#
        title=Label(Frame_login,text="Login Here",font=("Bahnschrift Light",35,"bold"),fg="#2B547E",bg="#DEE4E7").place(x=90,y=30)
        Description=Label(Frame_login,text="Admin Login",font=("Bahnschrift Light",15,"bold"),fg="#2B547E",bg="#DEE4E7").place(x=90,y=100)

        #================Username=================#
        lbl_user=Label(Frame_login,text="Username",font=("Bahnschrift Light",13,"bold"),fg="gray",bg="#DEE4E7").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("Bahnschrift Light",14),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=300,height=35)
        
        #=================Password=================#
        lbl_pass=Label(Frame_login,text="Password",font=("Bahnschrift Light",13,"bold"),fg="gray",bg="#DEE4E7").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("Bahnschrift Light",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=300,height=35)
        
        #=================Forgot Password ==========#
        forget_btn=Button(Frame_login,text="Forgot Password",bg="#DEE4E7",fg="#2B547E",bd=0,cursor="hand2",font=("Bahnschrift Light",12)).place(x=90,y=280)
         
        #=================Login Button=============#
        login=Button(command=self.login,text="Login",fg="white",bg="#2B547E",cursor="hand2",font=("Bahnschrift Light",20)).place(x=600,y=450,width=170,height=38)

    def login(self):
        
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get() =="admin" and self.txt_user.get() =="admin" :
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password:{self.txt_pass.get()}",parent=self.root)
            os.system("python Dashboard.py")
            self.root.destroy()
        elif self.txt_pass.get()=="123456" and self.txt_user.get()== "sriharsha":
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password:{self.txt_pass.get()}",parent=self.root)
            os.system("python Dashboard.py")
            self.root.destroy()
        else:
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
root=Tk()
obj=Login(root)
root.mainloop()