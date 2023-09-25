from tkinter import* 
from tkinter import ttk,messagebox
from PIL import ImageTk
import sqlite3
class resultClass:

    def __init__(self,root):
        self.root=root
        self.root.title("College Management System")
        self.root.geometry("1520x785+0+0")
        self.root.config(bg="#DEE4E7")

        title=Label(self.root,text="Manage Student Result",font=("Bahnschrift Light",20,"bold"),bg="#86608E",fg="white").place(x=10,y=15,width=1500,height=50)
        
        new_lbl=Label(self.root,text="Add Student Result Here",font=("Bahnschrift Light",25,"bold"),bg="#DEE4E7",fg="#154360").place(x=80,y=145,width=450,height=50)

        #=========================Image===========#
        self.bg=ImageTk.PhotoImage(file="amity.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=750,y=70,width=500,height=580)
        #=========================Widgets=====================#
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()
        lbl_select=Label(self.root,text="Student Roll No.",font=("Bahnschrift Light",18,"bold"),bg="#DEE4E7",fg="#154360").place(x=40,y=250)
        lbl_name=Label(self.root,text="Name",font=("Bahnschrift Light",20,"bold"),bg="#DEE4E7",fg="#154360").place(x=40,y=340)
        lbl_course=Label(self.root,text="Course",font=("Bahnschrift Light",20,"bold"),bg="#DEE4E7",fg="#154360").place(x=40,y=400)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("Bahnschrift Light",20,"bold"),bg="#DEE4E7",fg="#154360").place(x=40,y=460)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("Bahnschrift Light",20,"bold"),bg="#DEE4E7",fg="#154360").place(x=40,y=520)
   
        txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("Bahnschrift Light",15,"bold"),state='readonly',justify=CENTER).place(x=300,y=250,width=200)
        btn_search=Button(self.root,text="Search",font=("Bahnschrift Light",16,"bold"),bg="#20B2AA",fg="white",cursor="hand2",command=self.search).place(x=520,y=250,width=100,height=28)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("Bahnschrift Light",20,"bold"),bg="white",state='readonly').place(x=300,y=340,width=220)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("Bahnschrift Light",20,"bold"),bg="white",state='readonly').place(x=300,y=400,width=220)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("Bahnschrift Light",20,"bold"),bg="white").place(x=300,y=460,width=220)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("Bahnschrift Light",20,"bold"),bg="white").place(x=300,y=520,width=220)

        btn_add=Button(self.root,text="Submit",font=("Bahnschrift Light",15),bg="#A52A2A",fg="white",cursor="hand2",command=self.add).place(x=210,y=585,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("Bahnschrift Light",15),bg="#696969",fg="white",cursor="hand2",command=self.clear).place(x=350,y=585,width=120,height=35)
        
    def fetch_roll(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            row=cur.fetchall()
            if len(row)>0:
                for row in row:
                  self.roll_list.append(row[0])
        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
     
    def search(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def add(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Result already present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(),
                    str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    def clear(self):
        self.var_roll.set(""),
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")
        self.root.destroy()
    
if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()