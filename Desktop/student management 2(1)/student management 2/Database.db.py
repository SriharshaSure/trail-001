import sqlite3
def create_db():
    con=sqlite3.connect(database="student_Data.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,course text,gender text,dob text,blood text,email text,contact text,country text,state text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    con.close()

create_db()