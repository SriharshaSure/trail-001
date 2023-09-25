from tkinter import* 
from tkinter import ttk,messagebox
from typing import Pattern
from PIL import ImageTk
import sqlite3
class reportClass:
   def __init__(self,root):
        self.root=root
        self.root.title("College Management System")
        self.root.geometry("1500x785+0+0")
        self.root.config(bg="#DEE4E7")

        title=Label(self.root,text="View Student Result",font=("Bahnschrift Light",20,"bold"),bg="#86608E",fg="white").place(x=10,y=15,width=1500,height=50)
     #====================Search=====================#
        self.var_search=StringVar()
        lbl_search=Label(self.root,text="Search By Roll No:",font=("Bahnschrift Light",20,"bold"),bg="#DEE4E7",fg="#154360").place(x=390,y=170)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("Bahnschrift Light",20),bg="white",fg="#154360").place(x=660,y=170,width=180)
        btn_search=Button(self.root,text="Search",font=("Bahnschrift Light",15,"bold"),bg="#20B2AA",fg="white",cursor="hand2",command=self.search).place(x=870,y=170,width=100,height=35)


     #===================Labels=======================#
        lbl_roll=Label(self.root,text="Roll No",font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN).place(x=290,y=300,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN).place(x=440,y=300,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN).place(x=590,y=300,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN).place(x=740,y=300,width=170,height=50)
        lbl_full=Label(self.root,text="Total Marks",font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN).place(x=910,y=300,width=160,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN).place(x=1060,y=300,width=170,height=50)

        self.roll=Label(self.root,font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN)
        self.roll.place(x=290,y=350,width=150,height=50)
        self.name=Label(self.root,font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN)
        self.name.place(x=440,y=350,width=150,height=50)
        self.course=Label(self.root,font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN)
        self.course.place(x=590,y=350,width=150,height=50)
        self.marks=Label(self.root,font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN)
        self.marks.place(x=740,y=350,width=170,height=50)
        self.full=Label(self.root,font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN)
        self.full.place(x=910,y=350,width=160,height=50)
        self.per=Label(self.root,font=("Bahnschrift Light",15,"bold"),bg="white",fg="#154360",bd=2,relief=SUNKEN)
        self.per.place(x=1060,y=350,width=170,height=50)


        
        btn_clear=Button(self.root,text="Clear",font=("Bahnschrift Light",15,"bold"),bg="#696969",fg="white",cursor="hand2",command=self.clear).place(x=660,y=450,width=150,height=35)

        failure=Label(self.root,text="Success Consists of going from Failure to Failure without loss of Enthusiasm !!! ",font=("Bahnschrift Light",20,"bold"),bg="#696969",fg="white").place(x=10,y=695,width=1500,height=50)

 #======================================================================================#
   def search(self):
         con=sqlite3.connect(database="studentdata.db")
         cur=con.cursor()
         try:
            if self.var_search.get()=="":
              messagebox.showerror("Error","Roll no. is required",parent=self.root)
            else:
               cur.execute("select * from result where roll=?",(self.var_search.get(),))
               row=cur.fetchone()
               if row!=None:
                  self.roll.config(text=row[1])
                  self.name.config(text=row[2])
                  self.course.config(text=row[3])
                  self.marks.config(text=row[4])
                  self.full.config(text=row[5])
                  self.per.config(text=row[6])
               else:
                   messagebox.showerror("Error","No Record Found",parent=self.root)
         except Exception as ex:
                   messagebox.showerror("Error",f"Error due to {str(ex)}")

   def clear(self):
               self.var_id=""
               self.roll.config(text="")
               self.name.config(text="")
               self.course.config(text="")
               self.marks.config(text="")
               self.full.config(text="")
               self.per.config(text="")
               self.var_search.set("")

if __name__=="__main__":
      root=Tk()
      obj=reportClass(root)
      root.mainloop()