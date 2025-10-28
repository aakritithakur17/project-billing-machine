from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox

root = Tk()
root.title("MySQL Form")
root.geometry("400x300")

def conn():
    name = e.get()
    age = e1.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "Fill all fields")
    else:
        try:
            
            con = mysql.connect(
                host="localhost",
                user="root",
                password="Th@kur17",
                database="bill_machine"   
            )
            mycursor = con.cursor()

            
            s = "INSERT INTO tbl (name, age) VALUES (%s, %s)"
            v = (name, int(age))   

            mycursor.execute(s, v)
            con.commit()

            messagebox.showinfo("Success", "Record inserted successfully")

        except Exception as ex:
            messagebox.showerror("Database Error", str(ex))

        finally:
            if con.is_connected():
                mycursor.close()
                con.close()


Label(root, text="Name").place(x=100, y=100)
e = Entry(root, width=30)
e.place(x=150, y=100)

Label(root, text="Age").place(x=100, y=150)
e1 = Entry(root, width=30)
e1.place(x=150, y=150)

btn = Button(root, text="Submit", padx=20, pady=10, command=conn)
btn.place(x=170, y=200)

root.mainloop()