from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Managment")
root.resizable(False,False)

def Reset():
	print



Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa..........Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies......Rs.30/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea............Rs.7/plate",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Coffee........Rs.100/plate",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice.........Rs.20/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancake....Rs.15/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Eggs...........Rs.7/plate",fg="black",bg="lightgreen").place(x=10,y=260)

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

dosa=StringVar()
cookies=StringVar()
tea=StringVar()
coffee=StringVar()
juice=StringVar()
pancakes=StringVar()
eggs=StringVar()
total_bill=StringVar()


lbl_dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="blue4")
lbl_cookies=Label(f1,font=("aria",20,"bold"),text="Cookies",width=12,fg="blue4")
lbl_tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="blue4")
lbl_coffee=Label(f1,font=("aria",20,"bold"),text="Coffee",width=12,fg="blue4")
lbl_juice=Label(f1,font=("aria",20,"bold"),text="Juice",width=12,fg="blue4")
lbl_pancakes=Label(f1,font=("aria",20,"bold"),text="PanCakes",width=12,fg="blue4")
lbl_eggs=Label(f1,font=("aria",20,"bold"),text="Eggs",width=12,fg="blue4")

lbl_dosa.grid(row=1,column=0)
lbl_cookies.grid(row=2,column=0)
lbl_tea.grid(row=3,column=0)
lbl_coffee.grid(row=4,column=0)
lbl_juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_eggs.grid(row=7,column=0)

entry_dosa=Entry(f1,font=("aria",20,"bold"),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_dosa.grid(row=1,column=1)

entry_cookies=Entry(f1,font=("aria",20,"bold"),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_cookies.grid(row=2,column=1)

entry_tea=Entry(f1,font=("aria",20,"bold"),textvariable=tea,bd=6,width=8,bg="lightpink")
entry_tea.grid(row=3,column=1)

entry_coffee=Entry(f1,font=("aria",20,"bold"),textvariable=coffee,bd=6,width=8,bg="lightpink")
entry_coffee.grid(row=4,column=1)

entry_juice=Entry(f1,font=("aria",20,"bold"),textvariable=juice,bd=6,width=8,bg="lightpink")
entry_juice.grid(row=5,column=1)

entry_pancakes=Entry(f1,font=("aria",20,"bold"),textvariable=pancakes,bd=6,width=8,bg="lightpink")
entry_pancakes.grid(row=6,column=1)

entry_eggs=Entry(f1,font=("aria",20,"bold"),textvariable=eggs,bd=6,width=8,bg="lightpink")
entry_eggs.grid(row=7,column=1)


btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font("arial",16."bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)








root.mainloop()