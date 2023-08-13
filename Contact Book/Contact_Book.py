from tkinter import *
from tkinter import messagebox
import cx_Oracle

root = Tk()
root.title("Contact Book")
root.geometry("800x620")
root.configure(bg="steel blue")

fname = StringVar()
lname = StringVar()
phone = IntVar()
email = StringVar()
address = StringVar()
pin = IntVar()

def sno():
    con = cx_Oracle.connect("your connection path")
    cursor = con.cursor()
    cursor.execute("select sno from contact_book")
    s = cursor.fetchall()  
    con.close()
    return s[-1][0]+1 

def save():
    f = fname.get()
    l = lname.get()
    p = phone.get()
    e = email.get()
    a = address.get()
    pi = pin.get()
    
    con = cx_Oracle.connect("your connection path")
    cursor = con.cursor()
    cursor.execute("insert into contact_book values(&sno,&fname,&lname,&phone,&email,&address,&pin)",(sno(),f,l,p,e,a,pi))
    con.commit()

    messagebox.showinfo("Information","Your contact has added.")
    con.close()
def reset():
    fname.set("")
    lname.set("")
    phone.set("")
    email.set("")
    address.set("")
    pin.set("")
    
def contactl():
    contact = Toplevel()
    contact.title("Contact list")
    contact.geometry("1500x600")
    contact.configure(bg="steel blue")
    top = Label(contact,text="Contact List",width=20,fg="Green",font=("vardana",16,"bold")).pack()
    listl = Label(contact,text="Saved Contact List →",bg="steel blue",fg="orange",font=("vardana",15,"bold")).place(x=70,y=70)
    lst = ['S.No','Fname','Lname','Phone','E-mail','Address','PinCode']
    m = 50
    for i in lst:
        dt = Label(contact,text=i,width=15,fg="blue",font=("vardana",14,"bold")).place(x=m,y=100)
        m = m+200

    con = cx_Oracle.connect("your connection path")
    cursor = con.cursor()
    cursor.execute("select * from contact_book")
    data = cursor.fetchall()
    con.commit()
    con.close()

    a = 50
    b = 135
    for i in data:
        for j in i:
            dt = Label(contact,text=j,width=22,fg="black",font=("vardana",10,"bold")).place(x=a,y=b)
            a = a+200
        b = b+30
        a = 50

    contact.mainloop()

top = Label(root,text="Contact Book",width=20,fg="Green",font=("vardana",20,"bold")).pack()
listlbl = Label(root,text="Click to List the contact →",bg="steel blue",fg="red",font=("vardana",15,"bold")).place(x=150,y=80)
contact_list = Button(root,text="Contact List",bg="white",fg="black",font=("vardana",13,"bold"),command=contactl).place(x=450,y=80)

frame = Frame(root,width=600,height=480,bg="gray").place(x=100,y=130)
lbl = Label(frame,text="Create New Contact",bg="gray",fg="orange",font=("vardana",18,"bold")).place(x=120,y=140)
fnamelbl = Label(frame,text="First Name",bg="gray",fg="white",font=("vardana",15,"bold")).place(x=250,y=180)
fnamee = Entry(frame,textvariable=fname,bg="white",fg="green",font=("vardana",15,"bold")).place(x=250,y=210)
lnamelbl = Label(frame,text="Last Name",bg="gray",fg="white",font=("vardana",15,"bold")).place(x=250,y=250)
lnamelble = Entry(frame,textvariable=lname,bg="white",fg="green",font=("vardana",15,"bold")).place(x=250,y=280)
phonelbl = Label(frame,text="Phone",bg="gray",fg="white",font=("vardana",15,"bold")).place(x=250,y=320)
phonee = Entry(frame,textvariable=phone,bg="white",fg="green",font=("vardana",15,"bold")).place(x=250,y=350)
emaillbl = Label(frame,text="E-mail",bg="gray",fg="white",font=("vardana",15,"bold")).place(x=250,y=390)
emailse = Entry(frame,textvariable=email,bg="white",fg="green",font=("vardana",15,"bold")).place(x=250,y=420)
addresslbl = Label(frame,text="Address",bg="gray",fg="white",font=("vardana",15,"bold")).place(x=250,y=460)
addresse = Entry(frame,textvariable=address,bg="white",fg="green",font=("vardana",15,"bold")).place(x=250,y=490)
pinlbl = Label(frame,text="Pin",bg="gray",fg="white",font=("vardana",15,"bold")).place(x=250,y=530)
pinse = Entry(frame,textvariable=pin,bg="white",fg="green",font=("vardana",15,"bold")).place(x=250,y=560)

# button
saveb = Button(root,text="Save",width=8,bg="white",fg="black",font=("vardana",13,"bold"),command=save).place(x=120,y=200)
resetb = Button(root,text="Reset",width=8,bg="white",fg="black",font=("vardana",13,"bold"),command=reset).place(x=120,y=260)

root.mainloop()
