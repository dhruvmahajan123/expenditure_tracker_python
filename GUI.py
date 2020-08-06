from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from datetime import date
import database as db
#from database import *
 
 
def Addexpense():
    a=date.today()
    b=Title.get()
    c=Expense.get()
 
    d=cname.get()
    data=[a,b,c]
    print(data)
    TVExpense.insert('','end',values=data)
    db.addDebit(d,b,int(c))
 
 
def Addincome():
    a=date.today()
    b=Title1.get()
    c=Income.get()
    d=aname.get()
    data=[a,b,c]
    print(data)
    TVIncome.insert('','end',values=data)
    db.addCredit(d,b,int(c))
 
def Deleteexpense():
    TVExpense.delete(*TVExpense.get_children())
 
def Deleteincome():
    TVIncome.delete(*TVIncome.get_children())
 
def Reg():
    a=name.get()
    db.init(a)
 
def ViewC():
    TVExpense4.delete(*TVExpense4.get_children())
    hge=ttk.Label(F4,text='                                               ',font=(None,18))
    hge.grid(row=6,column=1,padx=5,pady=5,sticky='w')
    total=0
    d=rand.get()
    data=list(db.viewCredit(d))
    for i in range(len(data)):
        temp=list(data[i])
        total+=temp[2]
        TVExpense4.insert('','end',values=temp)
    abcde=ttk.Label(F4,text='Total Credit:'+str(total),font=(None,18))
    abcde.grid(row=6,column=1,padx=5,pady=5,sticky='w')
 
 
 
 
def ViewD():
    TVExpense5.delete(*TVExpense5.get_children())
    hg=ttk.Label(F4,text='                                               ',font=(None,18))
    hg.grid(row=6,column=2,padx=5,pady=5,sticky='w')
    total=0
    a=date.today()
    b=Title.get()
    c=Expense.get()
    d=rand.get()
    data=list(db.viewDebit(d))
    for i in range(len(data)):
        temp=list(data[i])
        total+=temp[2]
        TVExpense5.insert('','end',values=temp)
    abcd=ttk.Label(F4,text='Total Debit:'+str(total),font=(None,18))
    abcd.grid(row=6,column=2,padx=5,pady=5,sticky='w')

 
 
 
 
GUI=Tk()
GUI.title('ManaJe')
GUI.geometry('700x500')
#GUI.state('zoomed')
scrollbar = Scrollbar(GUI)
scrollbar.pack( side = RIGHT, fill = Y )
 
 
Tab=Notebook(GUI)
 
F1=Frame(Tab,width=500,height=500)
F2=Frame(Tab,width=500,height=500)
F3=Frame(Tab,width=500,height=500)
F4=Frame(Tab,width=500,height=500)
 
Tab.add(F1,text='Register')
Tab.add(F2,text='Debt')
Tab.add(F3,text='Credit')
Tab.add(F4,text='View')
 
Tab.pack(fill=BOTH,expand=1)
 
 
#Tab1(Registration)
 
 
#-----Name-------------
Greet=ttk.Label(F1,text='MAKE AN ACCOUNT',font=("Times",25))
Greet.grid(row=1,column=6,padx=0,pady=10,sticky='w')
buffer=ttk.Label(F1,text='',font=(None,30))
buffer.grid(row=2,column=2,padx=60,pady=60,sticky='w')
LName=ttk.Label(F1,text='Name',font=("Times",20))
LName.grid(row=3,column=5,padx=4,pady=5,sticky='w')
 
name=StringVar()
 
EName=ttk.Entry(F1,textvariable=name,font=("Times",18))
EName.grid(row=3,column=6,padx=5,pady=5,sticky='w')
 
#----------Open------------------
 
BFCreate=ttk.Button(F1,text='OK',command=Reg)
BFCreate.grid(row=3,column=7,padx=6,pady=5,sticky='w')
 
 
#Tab2(Expense)
 
#-------Row 0---------
LDate=ttk.Label(F2,text='Date:',font=("Times",18))
LDate.grid(row=0,column=0,padx=5,pady=5,sticky='w')
 
today=date.today()
 
EDate=ttk.Label(F2,text=today,font=("Times",18))
EDate.grid(row=0,column=1,padx=5,pady=5,sticky='w')
 
#-------Row 1---------
LTitle=ttk.Label(F2,text='Title:',font=("Times",18))
LTitle.grid(row=1,column=0,padx=5,pady=5,sticky='w')
 
Title=StringVar()
 
ETitle=ttk.Entry(F2,textvariable=Title,font=("Times",18))
ETitle.grid(row=1,column=1,padx=5,pady=5,sticky='w')
 
#-------Row 2---------
 
CName=ttk.Label(F2,text='Name:',font=("Times",18))
CName.grid(row=2,column=0,padx=5,pady=5,sticky='w')
 
cname=StringVar()
 
DName=ttk.Entry(F2,textvariable=cname,font=("Times",18))
DName.grid(row=2,column=1,padx=5,pady=5,sticky='w')
 
#-------Row 3---------
LExpense=ttk.Label(F2,text='Debt:',font=("Times",18))
LExpense.grid(row=3,column=0,padx=5,pady=5,sticky='w',ipady=10)
 
Expense=StringVar()
 
EExpense=ttk.Entry(F2,textvariable=Expense,font=("Times",18))
EExpense.grid(row=3,column=1,padx=5,pady=5,sticky='w')
 
#----------Row 4------------
 
BF1Add=ttk.Button(F2,text='Add',command=Addexpense)
BF1Add.grid(row=4,column=1,padx=5,pady=5,sticky='w')
 
BF1Delete=ttk.Button(F2,text='Clear Table',command=Deleteexpense)
BF1Delete.grid(row=4,column=2,padx=5,pady=5,sticky='w')
 
 
#----------Tree View-----------
 
TVList=['Date','Title','Credit']
TVExpense=ttk.Treeview(F2,column=TVList,show='headings',height=10)
for i in TVList:
    TVExpense.heading(i,text=i.title())
TVExpense.grid(row=5,column=0,padx=50,pady=5,sticky='w',columnspan=3)
 
 
#Tab3(Income)
#-------Row 0---------
RDate=ttk.Label(F3,text='Date:',font=("Times",18))
RDate.grid(row=0,column=0,padx=5,pady=5,sticky='w')
 
today1=date.today()
 
FDate=ttk.Label(F3,text=today1,font=("Times",18))
FDate.grid(row=0,column=1,padx=5,pady=5,sticky='w')
 
#-------Row 1---------
RTitle=ttk.Label(F3,text='Title:',font=("Times",18))
RTitle.grid(row=1,column=0,padx=5,pady=5,sticky='w')
 
Title1=StringVar()
 
FTitle=ttk.Entry(F3,textvariable=Title1,font=("Times",18))
FTitle.grid(row=1,column=1,padx=5,pady=5,sticky='w')
 
#-------Row 2---------
 
AName=ttk.Label(F3,text='Name:',font=("Times",18))
AName.grid(row=2,column=0,padx=5,pady=5,sticky='w')
 
aname=StringVar()
 
BName=ttk.Entry(F3,textvariable=aname,font=("Times",18))
BName.grid(row=2,column=1,padx=5,pady=5,sticky='w')
 
#--------Row3----------
RIncome=ttk.Label(F3,text='Credit:',font=("Times",18))
RIncome.grid(row=3,column=0,padx=5,pady=5,sticky='w',ipady=10)
 
Income=StringVar()
 
FIncome=ttk.Entry(F3,textvariable=Income,font=("Times",18))
FIncome.grid(row=3,column=1,padx=5,pady=5,sticky='w')
 
#----------Row 4------------
 
BF2Add=ttk.Button(F3,text='Add',command=Addincome)
BF2Add.grid(row=4,column=1,padx=5,pady=5,sticky='w')
 
BF2Delete=ttk.Button(F3,text='Clear Table',command=Deleteincome)
BF2Delete.grid(row=4,column=2,padx=5,pady=5,sticky='w')
 
 
#----------Tree View-----------
 
TVList1=['Date','Title','Debt']
TVIncome=ttk.Treeview(F3,column=TVList1,show='headings',height=10)
for i in TVList1:
    TVIncome.heading(i,text=i.title())
TVIncome.grid(row=5,column=0,padx=50,pady=5,sticky='w',columnspan=3)
 
 
#Tab4(View)
cred=ttk.Label(F4,text='Credit Table',font=("Times",15))
cred.grid(row=0,column=1,padx=130,pady=5,sticky='w')
TVList4=['Date','Title','Credit']
TVExpense4=ttk.Treeview(F4,column=TVList,show='headings',height=5)
for i in TVList4:
    TVExpense4.heading(i,text=i.title())
TVExpense4.grid(row=1,column=0,padx=50,pady=5,sticky='w',columnspan=3)
scrollbar.config(command=TVList4)
deb=ttk.Label(F4,text='Debit Table',font=("Times",15))
deb.grid(row=2,column=1,padx=130,pady=5,sticky='w')
 
TVList5=['Date','Title','Debt']
TVExpense5=ttk.Treeview(F4,column=TVList5,show='headings',height=5)
for i in TVList5:
    TVExpense5.heading(i,text=i.title())
TVExpense5.grid(row=3,column=0,padx=50,pady=10,sticky='w',columnspan=3)
scrollbar.config(command=TVList5)
xyz=ttk.Label(F4,text='Name',font=("Times",18))
xyz.grid(row=4,column=0,padx=20,pady=5,sticky='w',ipady=10)
 
rand=StringVar()
 
rand2=ttk.Entry(F4,textvariable=rand,font=("Times",18))
rand2.grid(row=4,column=1,padx=5,pady=5,sticky='w')
 
 
 
var1=ttk.Button(F4,text='View Credit',command=ViewC)
var1.grid(row=5,column=1,padx=5,pady=5,sticky='w')
var2=ttk.Button(F4,text='View Debt',command=ViewD)
var2.grid(row=5,column=2,padx=5,pady=5,sticky='w')
 
 
 
GUI.mainloop()
#