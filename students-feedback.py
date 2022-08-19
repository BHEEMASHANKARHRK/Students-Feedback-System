import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['name'])
    e2.insert(0, select['vtuno'])
    e3.insert(0, select['sem'])
    e4.insert(0, select['gmail'])
    e5.insert(0, select['teacher_name'])
    e6.insert(0, select['subject_name'])
    e7.insert(0, select['feedback_option'])


def Add():
    name = e1.get()
    vtuno = e2.get()
    sem = e3.get()
    gmail= e4.get()
    teacher_name=e5.get()
    subject_name=e6.get()
    feedback_option=e7.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="feed_back")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  student_feedback (name,vtuno,sem,gmail,teacher_name,subject_name,feedback_option) VALUES (%s, %s, %s, %s, %s, %s, %s)"
       val = (name,vtuno,sem,gmail,teacher_name,subject_name,feedback_option)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", " inserted record successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e6.delete(0, END)
       e7.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()



def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="feed_back")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT name,vtuno,sem,gmail,teacher_name,subject_name,feedback_option FROM student_feedback")
        records = mycursor.fetchall()
        print(records)

        for i, (name, vtuno, sem, gmail, teacher_name, subject_name,feedback_option) in enumerate(records, start=1):
            listBox.insert("", "end", values=(name,vtuno, sem, gmail, teacher_name, subject_name,feedback_option))
            mysqldb.close()

root = Tk()


root.geometry("10000x10000")
root.title("STUDENTS FEEDBACK")

def submit():
        global e1
        global e2
        global e3
        global e4
        global e5
        global e6
        global e7

tk.Label(root, text="STUDENTS  FEEDBACK", fg="blue", font=("Algerian", 30)).place(x=450, y=5)

Label(root, text="NAME :",fg="orange",font=(None, 10)).place(x=250, y=80)
Label(root, text="VTU_NO  :",fg="orange",font=(None, 10)).place(x=250, y=110)
Label(root, text="SEM  :",fg="orange",font=(None, 10)).place(x=250, y=140)
Label(root, text="GMAIL_ID :",fg="orange",font=(None, 10)).place(x=250, y=170)
Label(root, text="TEACHER_NAME:",fg="orange",font=(None, 10)).place(x=250, y=200)
Label(root, text="SUBJECT_NAME:",fg="orange",font=(None, 10)).place(x=250,y=230)
Label(root, text="FEEDBACK:",fg="orange",font=(None, 10)).place(x=250,y=300)

Label(root, text="1]  Poor    \n "
                 "      2]  Satisfactory\n"
                 "3]    Good\n"
                 "      4]  Very Good\n"
                 "     5]  Excellent\n",fg="red",font=(None, 10)).place(x=600,y=300)


e1 = Entry(root)
e1.place(x=450, y=80)

e2 = Entry(root)
e2.place(x=450, y=110)

e3 = Entry(root)
e3.place(x=450, y=140)

e4 = Entry(root)
e4.place(x=450, y=170)

e5 = Entry(root)
e5.place(x=450, y=200)

e6 = Entry(root)
e6.place(x=450, y=230)

e7= Entry(root)
e7.place(x=450,y=300)


Button(root, text="Submit",command=Add,height=3, width= 10).place(x=500, y=400)


Button(root,text="Show",command=show,height=3,width=10).place(x=990,y=400)


cols = ('name', 'vtuno', 'sem','gamil','teacher_name','subject_name','feedback_option')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=100)
    listBox.place(x=50, y=500)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()