from tkinter import*
from tkinter import ttk,messagebox
import sqlite3
class studentClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Result Management System")
        self.root.geometry("1520x785+0+0")
        self.root.config(bg="#DEE4E7")

        title=Label(self.root,text="Manage student Details",font=("Bahnschrift Light",20,"bold"),bg="#86608E",fg="white").place(x=0,y=0,relwidth=1,height=50)
        add_student=Label(self.root,text="Add student Details",font=("Bahnschrift Light",30,"bold"),bg="#DEE4E7",fg="#154360").place(x=200,y=100)
        

        #========================================Variable Declaration====================================#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_blood=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_country=StringVar()
        self.var_state=StringVar()
        self.var_search=StringVar()
        
        #==============Labels============#
        lbl_roll=Label(self.root,text="Roll No*",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=180)
        lbl_name=Label(self.root,text="Name",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=260)
        lbl_course=Label(self.root,text="Course",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=300)
        lbl_gender=Label(self.root,text="Gender",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=340)
        lbl_dob=Label(self.root,text="DOB",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=380)
        lbl_blood=Label(self.root,text="Blood Group",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=420)
        lbl_email=Label(self.root,text="Email",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=460)
        lbl_contact=Label(self.root,text="Contact",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=500)
        lbl_country=Label(self.root,text="Country",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=540)
        lbl_state=Label(self.root,text="State",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=215,y=220)
        

     
        #==============Entry===========================#
        self.txt_roll=Entry(self.root,textvariable=self.var_roll,font=("Bahnschrift Light",15,"bold"),fg="#800080")
        self.txt_roll.place(x=315,y=180,width=200)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("Bahnschrift Light",15,"bold"),fg="#800080").place(x=315,y=260,width=200)
        #function call to update the list
        self.course_list=['B.Tech CSE','B.Tech CE','B.Tech ECE','B.Tech AE','B.Tech Biotech','B.Tech Mechanical','B.Sc.-Nursing','BCA','BBA','MBA','B.Pharmacy','BDS','BA','B.Com','B.Ed']
        txt_course=ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("Bahnschrift Light",15,"bold"),state='readonly',justify=CENTER).place(x=315,y=300,width=200)
        txt_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Male","Female","Other"),font=("Bahnschrift Light",15,"bold"),state='readonly',justify=CENTER).place(x=315,y=340,width=200)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("Bahnschrift Light",15,"bold"),fg="#800080").place(x=315,y=380,width=170)
        txt_blood=ttk.Combobox(self.root,textvariable=self.var_blood,values=("A+","B+","O+","AB+","A-","B-","O-","AB-"),font=("Bahnschrift Light",15,"bold"),state='readonly',justify=CENTER).place(x=365,y=420,width=120)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("Bahnschrift Light",15,"bold"),fg="#800080").place(x=315,y=460,width=200)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("Bahnschrift Light",15,"bold"),fg="#800080").place(x=315,y=500,width=200)
        txt_country=Entry(self.root,textvariable=self.var_country,font=("Bahnschrift Light",15,"bold"),fg="#800080").place(x=315,y=540,width=200)
        txt_state=Entry(self.root,textvariable=self.var_state,font=("Bahnschrift Light",15,"bold"),fg="#800080").place(x=315,y=220,width=200)        
        
        #========================Buttons================#
        self.btn_save=Button(self.root,text='Save',font=("Bahnschrift Light",15,"bold"),bg="#800080",fg="white",cursor="hand2",command=self.add)
        self.btn_save.place(x=150,y=580,width=110,height=40)
        self.btn_update=Button(self.root,text='Update',font=("Bahnschrift Light",15,"bold"),bg="#008080",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=580,width=110,height=40)
        self.btn_delete=Button(self.root,text='Delete',font=("Bahnschrift Light",15,"bold"),bg="#DC143C",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=580,width=110,height=40)
        self.btn_clear=Button(self.root,text='Clear',font=("Bahnschrift Light",15,"bold"),bg="#696969",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=580,width=110,height=40)
        
        #================Search Panel========================#
        lbl_search_roll=Label(self.root,text="Roll No",font=("Bahnschrift Light",15,"bold"),bg="#DEE4E7",fg="#154360").place(x=870,y=60)
        txt_search_roll=Entry(self.root,textvariable=self.var_search,font=("Bahnschrift Light",15,"bold"),bg="white").place(x=970,y=60,width=140)
        btn_search=Button(self.root,text="Search",font=("Bahnschrift Light",15,"bold"),bg="#20B2AA",fg="white",cursor="hand2",command=self.search).place(x=1130,y=60,width=120,height=28)
        
        self.C_Frame=Frame(self.root,bd=6,relief=SUNKEN)
        self.C_Frame.place(x=650,y=100,width=600,height=550)
        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("roll","name","course","gender","dob","blood","email","contact","country","state"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrollx.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("roll",text="Roll No.")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("gender",text="Gender")
        self.CourseTable.heading("dob",text="DOB")
        self.CourseTable.heading("blood",text="Blood Group")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("country",text="Country")
        self.CourseTable.heading("state",text="State")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",anchor=CENTER,width=50)
        self.CourseTable.column("name",anchor=CENTER,width=80)
        self.CourseTable.column("course",anchor=CENTER,width=70)
        self.CourseTable.column("gender",anchor=CENTER,width=50)
        self.CourseTable.column("dob",anchor=CENTER,width=50)
        self.CourseTable.column("blood",anchor=CENTER,width=50)
        self.CourseTable.column("email",anchor=CENTER,width=70)
        self.CourseTable.column("contact",anchor=CENTER,width=70)
        self.CourseTable.column("country",anchor=CENTER,width=50)
        self.CourseTable.column("state",anchor=CENTER,width=40)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        

    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_blood.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_country.set("")
        self.var_state.set("")
        self.txt_roll.config(state=NORMAL)

    def delete(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select student from the List first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really want to delete?",parent=self.root)
                if op==True:
                    cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","student Deleted Successfully",parent=self.root)
                    self.clear()

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")
        

    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_course.set(row[2])
        self.var_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_blood.set(row[5])
        self.var_email.set(row[6])
        self.var_contact.set(row[7])
        self.var_country.set(row[8])
        self.var_state.set(row[9])                                                                  
       
    
    def add(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No.should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Roll No Already present",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,course,gender,dob,blood,email,contact,country,state) values(?,?,?,?,?,?,?,?,?,?)",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_blood.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.var_country.get(),
                    self.var_state.get()
                    ))
                    con.commit()
                    self.show()
                    messagebox.showinfo("Success","student Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def update(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No should be required",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Select student from list",parent=self.root)
                else:
                    cur.execute("Update student set name=?,course=?,gender=?,dob=?,blood=?,email=?,contact=?,country=?,state=? where roll=?",(
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_blood.get(),
                    self.var_email.get(),
                    self.var_contact.get(),
                    self.var_country.get(),
                    self.var_state.get(),
                    self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","student Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def show(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            row=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in row:
               self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



    def search(self):
        con=sqlite3.connect(database="studentdata.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student where roll=?",(self.var_search.get(),))
            row=cur.fetchone()
            if row!=None:
               self.CourseTable.delete(*self.CourseTable.get_children())
               self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")



if __name__=="__main__":
    root=Tk()
    obj=studentClass(root)
    root.mainloop()