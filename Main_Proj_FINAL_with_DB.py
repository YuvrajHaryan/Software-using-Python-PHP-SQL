from tkinter import *
import time
from PIL import ImageTk,Image
import os
import mysql.connector
window = Tk() 
window.geometry("500x800")
window.title("WELCOME")
window.configure(background="green")
window.resizable(False,False)

lab = Label(window,text="PIZZA SHOP ",fg="red",bg="yellow",font="arial 30 bold")
lab.pack(anchor=CENTER)

def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 25')
    window.after(100,clock)
label1=Label(window,justify='center')
label1.pack(anchor=CENTER)
clock()

#count of items
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0
i8 = 0
T = 0
def p1():
    global i1
    global T
    i1=i1+1
    T=T+80
    lab1.config(text=i1)
    tot_lab.config(text=T)
def p2():
    global i2
    global T
    i2=i2+1
    T=T+90
    lab2.config(text=i2)
    tot_lab.config(text=T)
def p3():
    global i3
    global T
    i3=i3+1
    T=T+100
    lab3.config(text=i3)
    tot_lab.config(text=T)
def p4():
    global i4
    global T
    i4=i4+1
    T=T+110
    lab4.config(text=i4)
    tot_lab.config(text=T)
def p5():
    global i5
    global T
    i5=i5+1
    T=T+120
    lab5.config(text=i5)
    tot_lab.config(text=T)
def p6():
    global i6
    global T
    i6=i6+1
    T=T+130
    lab6.config(text=i6)
    tot_lab.config(text=T)
def p7():
    global i7
    global T
    i7=i7+1
    T=T+140
    lab7.config(text=i7)
    tot_lab.config(text=T)
def p8():
    global i8
    global T
    i8=i8+1
    T=T+150
    lab8.config(text=i8)
    tot_lab.config(text=T)


#Bill Window
def new_window():

    #Insert into DB
    n=entry1.get()
    m=entry2.get()
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="internship2_pizza_shop"
    )
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO cust_info(name,mobile_no) VALUES(%s,%s)",(n,m))
    db_connection.commit()
    print(db_cursor.rowcount, "Record Inserted")

    window1 = Tk() 
    window1.geometry("500x800")
    for rows in range (10):
        window1.grid_rowconfigure(rows,minsize=50)
        window1.grid_columnconfigure(rows,minsize=166)
    window1.title("BILL")
    window1.configure(background="red")
    window1.resizable(False,False)

    #Row No.
    r=2     

    w1_lab = Label(window1,text="BILL",fg="yellow",bg="green",font="arial 30 bold")
    w1_lab.grid(row=0,column=1,padx=35)

    w1_head1 = Label(window1,text="Pizza",fg="white",bg="yellow",font="arial 20 bold")
    w1_head1.grid(row=1,column=0,pady=20)
    w1_head2 = Label(window1,text="Qty",fg="white",bg="yellow",font="arial 20 bold")
    w1_head2.grid(row=1,column=1,pady=20)
    w1_head3 = Label(window1,text="Price",fg="white",bg="yellow",font="arial 20 bold")
    w1_head3.grid(row=1,column=2,pady=20)

    #item1
    if(i1>0):
        w1_lab111 = Label(window1,text="Veg Mexican",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab111.grid(row=r,column=0,pady=10)
        w1_lab11 = Label(window1,text="X"+str(i1),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab11.grid(row=r,column=1,pady=10)
        w1_lab1 = Label(window1,text=i1*80,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab1.grid(row=r,column=2,pady=10)
        r=r+1
    

    #item2
    if(i2>0):
        w1_lab222 = Label(window1,text="Veg Tomatino",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab222.grid(row=r,column=0,pady=10)
        w1_lab22 = Label(window1,text="X"+str(i2),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab22.grid(row=r,column=1,pady=10)
        w1_lab2 = Label(window1,text=i2*90,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab2.grid(row=r,column=2,pady=10)
        r=r+1


    #item3
    if(i3>0):
        w1_lab333 = Label(window1,text="Regular Veggie",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab333.grid(row=r,column=0,pady=10)
        w1_lab33 = Label(window1,text="X"+str(i3),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab33.grid(row=r,column=1,pady=10)
        w1_lab3 = Label(window1,text=i3*100,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab3.grid(row=r,column=2,pady=10)
        r=r+1


    #item4
    if(i4>0):
        w1_lab444 = Label(window1,text="Veg Oninon",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab444.grid(row=r,column=0,pady=10)
        w1_lab44 = Label(window1,text="X"+str(i4),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab44.grid(row=r,column=1,pady=10)
        w1_lab4 = Label(window1,text=i4*110,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab4.grid(row=r,column=2,pady=10)
        r=r+1


    #item5
    if(i5>0):
        w1_lab555 = Label(window1,text="Veg Jalpeno",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab555.grid(row=r,column=0,pady=10)
        w1_lab55 = Label(window1,text="X"+str(i5),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab55.grid(row=r,column=1,pady=10)
        w1_lab5 = Label(window1,text=i5*120,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab5.grid(row=r,column=2,pady=10)
        r=r+1


    #item6
    if(i6>0):
        w1_lab666 = Label(window1,text="Veg Peppy Paneer",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab666.grid(row=r,column=0,pady=10)
        w1_lab66 = Label(window1,text="X"+str(i6),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab66.grid(row=r,column=1,pady=10)
        w1_lab6 = Label(window1,text=i6*130,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab6.grid(row=r,column=2,pady=10)
        r=r+1


    #item7
    if(i7>0):
        w1_lab777 = Label(window1,text="Loaded Chicken",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab777.grid(row=r,column=0,pady=10)
        w1_lab77 = Label(window1,text="X"+str(i7),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab77.grid(row=r,column=1,pady=10)
        w1_lab7 = Label(window1,text=i7*140,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab7.grid(row=r,column=2,pady=10)
        r=r+1


    #item8
    if(i8>0):
        w1_lab888 = Label(window1,text="Chicken Chilli",fg="black",bg="white",font="arial 15 bold",width=14)
        w1_lab888.grid(row=r,column=0,pady=10)
        w1_lab88 = Label(window1,text="X"+str(i8),fg="yellow",bg="red",font="arial 10 bold",)
        w1_lab88.grid(row=r,column=1,pady=10)
        w1_lab8 = Label(window1,text=i8*150,fg="black",bg="white",font="arial 15 bold",width=5)
        w1_lab8.grid(row=r,column=2,pady=10)
        r=r+1


    #Total
    w1_total = Label(window1,text=" Total: ",fg="white",bg="green",font="arial 20 bold",height=2,width=7)
    w1_total.place(x=124, y=550)

    w1_tot_lab = Label(window1,text=T,fg="black",bg="white",font="arial 20 bold",width=7,height=2)
    w1_tot_lab.place(x=250, y=550)


    window1.mainloop()


#Database Info
name=Label(window,text="Name:",fg="Black",bg="green",font="arial 13 bold")
name.place(x=50,y=115)
entry1=Entry(window,font="arial 13",width=14)
entry1.place(x=110,y=115)
mob_no=Label(window,text="Mobile No:",fg="Black",bg="green",font="arial 13 bold")
mob_no.place(x=250,y=115)
entry2=Entry(window,font="arial 13",width=14)
entry2.place(x=340,y=115)


#item1
photo1 = PhotoImage(file="output1.png")
btn1=Button(window, text = 'Click Me !', image = photo1 ,height=50, width=50,command=p1)
btn1.place(x=40,y=150)

lab1 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab1.place(x=130, y=162.5)


#item2
photo2 = PhotoImage(file="output2.png")
btn2=Button(window, text = 'Click Me !', image = photo2 ,height=50, width=50,command=p2)
btn2.place(x=40,y=250)

lab2 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab2.place(x=130, y=262.5)


#item3
photo3 = PhotoImage(file="output3.png")
btn3=Button(window, text = 'Click Me !', image = photo3 ,height=50, width=50,command=p3)
btn3.place(x=40,y=350)

lab3 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab3.place(x=130, y=362.5)


#item4
photo4 = PhotoImage(file="output4.png")
btn4=Button(window, text = 'Click Me !', image = photo4 ,height=50, width=50,command=p4)
btn4.place(x=40,y=450)

lab4 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab4.place(x=130, y=462.5)


#item5
photo5 = PhotoImage(file="output5.png")
btn5=Button(window, text = 'Click Me !', image = photo5 ,height=50, width=50,command=p5)
btn5.place(x=300,y=150)

lab5 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab5.place(x=390, y=162.5)


#item6
photo6 = PhotoImage(file="output6.png")
btn6=Button(window, text = 'Click Me !', image = photo6 ,height=50, width=50,command=p6)
btn6.place(x=300,y=250)

lab6 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab6.place(x=390, y=262.5)


#item7
photo7 = PhotoImage(file="output7.png")
btn7=Button(window, text = 'Click Me !', image = photo7 ,height=50, width=50,command=p7)
btn7.place(x=300,y=350)

lab7 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab7.place(x=390, y=362.5)


#item8
photo8 = PhotoImage(file="output8.png")
btn8=Button(window, text = 'Click Me !', image = photo8 ,height=50, width=50,command=p8)
btn8.place(x=300,y=450)

lab8 = Label(window,text="",fg="black",bg="white",font="arial 15 bold",width=5)
lab8.place(x=390, y=462.5)

#Total
total = Label(window,text=" Total: ",fg="white",bg="brown",font="arial 20 bold",height=2,width=7)
total.place(x=124, y=550)

tot_lab = Label(window,text="",fg="black",bg="white",font="arial 20 bold",width=7,height=2)
tot_lab.place(x=250, y=550)


order_btn=Button(window, text = 'ORDER',fg="white",bg="red" ,font="arial 15 bold",height=1, width=14,command=new_window)
order_btn.place(x=160,y=630)


window.mainloop()
