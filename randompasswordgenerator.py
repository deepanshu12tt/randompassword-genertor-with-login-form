from tkinter import *
import random
import tkinter.messagebox as tsmg
def btn():
    print("The username is "+aval.get())
    print("The Age is " + bval.get())
    print("The Mobile Number is " + cval.get())
    print("The Country is " + dval.get())
    print("The State is " + eva.get())
    print("The city is " + fval.get())
    print("The District is " + gval.get())
    print("The Landmark is " + hval.get())
    tsmg.showinfo('Info',"The username is "+aval.get()+'\n'+"The Age is " +bval.get()+'\n'+"The Mobile Number is " +cval.get()+'\n'+"The Country is " +dval.get()+'\n'+"The State is " +eva.get()+'\n'+"The city is " +"The District is " +fval.get()+'\n'+gval.get()+'\n'+"The Landmark is " +hval.get())


def new():
    lower='abcdefghijklmnopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit='0123456789'
    symbol='!@#$%^&*,.;[](){}|?~'
    total=lower+upper+digit+symbol
    length=16
    passs=' '.join(random.sample(total,length))
    print("Te password is "+passs)
    tsmg.showinfo('Password',"The password is--> "+passs)
def neww():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digit = '0123456789'
    total=lower+upper+digit
    length=12
    password=' '.join(random.sample(total,length))
    print("The password is"+password)
    tsmg.showinfo('Password',"The password is-->"+password)

def newww():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    totol=lower+upper
    length=8
    password=' '.join(random.sample(totol,length))
    print("The password is "+password)
    tsmg.showinfo('Password',"The password is--> "+password)
root=Tk()
root.title('Password generator')
root.configure(bg='black')
root.geometry('700x700')
aval=StringVar()
bval=StringVar()
cval=StringVar()
dval=StringVar()
eva=StringVar()
fval=StringVar()
gval=StringVar()
hval=StringVar()
Label(root,text="Username").grid(row=17,column=7)
e=Entry(root,textvariable=aval).grid(row=17,column=8)
Label(root,text="Age").grid(row=18,column=7)
e=Entry(root,textvariable=bval).grid(row=18,column=8)
Label(root,text="Mobile Number").grid(row=19,column=7)
Entry(root,textvariable=cval).grid(row=19,column=8)
Label(root,text="Country").grid(row=20,column=7)
Entry(root,textvariable=dval).grid(row=20,column=8)
Label(root,text="State").grid(row=21,column=7)
Entry(root,textvariable=eva).grid(row=21,column=8)
Label(root,text="City").grid(row=22,column=7)
Entry(root,textvariable=fval).grid(row=22,column=8)
Label(root,text="District").grid(row=23,column=7)
Entry(root,textvariable=gval).grid(row=23,column=8)
Label(root,text="Landmark(optional)").grid(row=24,column=7)
Entry(root,textvariable=hval).grid(row=24,column=8)
Button(root,text='Click here',command=btn).grid(row=25,column=8)





b= Button(root,text=" Strong Password generator", command=new).grid(row=28,column=8)
b= Button(root,text=" Average  Password generator", command=neww).grid(row=29,column=8)
b= Button(root,text=" weak Password generator", command=newww).grid(row=30,column=8)

root.mainloop()