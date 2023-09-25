from tkinter import*
from tkinter import messagebox
from Student_Data import studentClass
from Add_Result import resultClass
from PIL import ImageTk
from View_Result import reportClass
import os
class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Pocket hospital")
        self.root.geometry("1520x785+0+0")
        self.root.config(bg="#DEE4E7")
        #=======================Title=================#
        title=Label(self.root,text="Student Management System",font=("Bahnschrift Light",20,"bold"),bg="#86608E",fg="white").place(x=0,y=0,relwidth=1,height=50)
        
        #=======================Image=======================#
        self.bg=ImageTk.PhotoImage(file="amitypic.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=10,y=130,width=1250,height=470)
        
        #====================Menu Frame==============#
        Menu_Frame=LabelFrame(self.root,text="Menu",font=("Bahnschrift Light",15),bg="#DEE4E7")
        Menu_Frame.place(x=10,y=70,width=1500,height=80)
        
        #=====================Buttons=================#
        btn_std=Button(Menu_Frame,text="student",font=("Bahnschrift Light",18,"bold"),bg="#154360",fg="white",cursor="hand2",command=self.add_student).place(x=80,width=190,height=40)
        btn_result=Button(Menu_Frame,text="Add Result",font=("Bahnschrift Light",18,"bold"),bg="#154360",fg="white",cursor="hand2",command=self.add_result).place(x=330,width=190,height=40)
        btn_view=Button(Menu_Frame,text="View Result",font=("Bahnschrift Light",18,"bold"),bg="#154360",fg="white",cursor="hand2",command=self.add_report).place(x=580,width=200,height=40)
        btn_logout=Button(Menu_Frame,text="Logout",font=("Bahnschrift Light",18,"bold"),bg="#154360",fg="white",cursor="hand2",command=self.logout).place(x=830,width=190,height=40)
        btn_exit=Button(Menu_Frame,text="Exit",font=("Bahnschrift Light",18,"bold"),bg="#154360",fg="white",cursor="hand2",command=self.exit).place(x=1070,width=170,height=40)
    

       #===========================Functions=========================#
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)
    
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        confirmation=messagebox.askyesno("Confirm","Do You really want to Log Out?",parent=self.root)
        if confirmation==True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        confirmation=messagebox.askyesno("Confirm","Do You really want to Exit?",parent=self.root)
        if confirmation==True:
            self.root.destroy()
        


if __name__=="__main__":
    root=Tk()
    obj=Dashboard(root)
    root.mainloop()