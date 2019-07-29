from tkinter import*
import math
import tkinter.messagebox
import parser
root=Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=FALSE,height=FALSE)
root.geometry("480x568+0+0")

calc=Frame(root)
calc.grid();

class Calc():
    def __init__(self):
        self.total=0
        self.current= ""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False
    def numberEnter(self,num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current=secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current=firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())

    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total -= self.current
        if self.op=="multi":
            self.total *= self.current
        if self.op=="divide":
            self.total /= self.current
        if self.op=="mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not  self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)

    def cos(self,x):
        self.result = False
        self.current = math.cos(x)
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
    def acosh(self):
        self.result = False
        self.current=math.acosh(float(txtDisplay.get()))
        self.display(self.current)
    def expm1(self):
        self.result = False
        self.current=math.expm1(float(txtDisplay.get()))
        self.display(self.current)
    def asinh(self):
        self.result = False
        self.current=math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current= math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def pow(self, x, n):
        self.result = False
        if x == 0 or x == 1 or n == 1:
            self.current= x

        if x == -1:
            if n % 2 == 0:
                self.current =1
            else:
                self.current=-1
        if n == 0:
            self.current= 1
        if n < 0:
            self.current= 1 / self.pow(x, -n)
        val = self.pow(x, n // 2)
        if n % 2 == 0:
            self.current=val * val
        self.current= val * val * x

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)
    def x2(self):
        self.result = False
        self.current=math.pow(float(txtDisplay.get()),2)
        self.display(self.current)

    def x3(self):
        self.result=False
        self.current=math.pow(float(txtDisplay.get()),3)
        self.display(self.current)
    def pm(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)
    def log10(self,x):
        self.result=False
        self.current=math.log10(x)
        self.display(self.current)
    def clearEntry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True
    def clearall(self):
        self.clearEntry()
        self.total=0







added_value=Calc()

txtDisplay=Entry(calc,font=('arial',20,'bold'),bg="powder blue",bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bg="white",bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x = numberpad [i]:added_value.numberEnter(x)
        i+=1
#==============================================Stadard Calculator=============================================================
btnclear=Button(calc,text=chr(67),width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.clearEntry).grid(row=1,column=1,pady=1)
btnallclear=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.clearEntry).grid(row=1,column=0,pady=1)
btnsq=Button(calc,text="√",width=6,height=2,font=('arial',20,'bold'),bg="powder blue").grid(row=1,column=2,pady=1)

btnplus=Button(calc,text="+",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=lambda:added_value.operation("add")
).grid(row=1,column=3,pady=1)
btnsub=Button(calc,text="-",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=lambda:added_value.operation("sub")).grid(row=2,column=3,pady=1)

btnmulti=Button(calc,text="x",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=lambda:added_value.operation("multi")).grid(row=3,column=3,pady=1)

btndiv=Button(calc,text="/",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=lambda:added_value.operation("divide")).grid(row=4,column=3,pady=1)
btnzero=Button(calc,text="0",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=lambda:added_value.numberEnter(0)
).grid(row=5,column=0,pady=1)

btndot=Button(calc,text=".",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=lambda:added_value.operation(".")).grid(row=5,column=1,pady=1)

btnnegate=Button(calc,text="±",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.pm).grid(row=5,column=2,pady=1)
btnequals=Button(calc,text="=",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.sum_of_total).grid(row=5,column=3,pady=1)



#=====================================================Scientific Calculator part========================================

btnpi=Button(calc,text="π",width=6,height=2,font=('arial',20,'bold'),bg="white",command=added_value.pi).grid(row=2,column=5,pady=1)
btncos=Button(calc,text="Cos",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value).grid(row=1,column=4,pady=1)#==================
btnsin=Button(calc,text="Sin",width=6,height=2,font=('arial',20,'bold'),bg="white").grid(row=2,column=4,pady=1)#============================================
btntan=Button(calc,text="Tan",width=6,height=2,font=('arial',20,'bold'),bg="white").grid(row=3,column=4,pady=1)#============================================
btncosh=Button(calc,text="Cosh",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.acosh).grid(row=1,column=5,pady=1)
btnsinh=Button(calc,text="Sinh",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.asinh).grid(row=3,column=6,pady=1)
btnlog=Button(calc,text="log",width=6,height=2,font=('arial',20,'bold'),bg="white",command=added_value).grid(row=4,column=4,pady=1)
btnexp=Button(calc,text="exp",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.exp).grid(row=5,column=4,pady=1)
btne=Button(calc,text="e",width=6,height=2,font=('arial',20,'bold'),bg="white",command=added_value.e).grid(row=3,column=5,pady=1)
btnmod=Button(calc,text="Mod",width=6,height=2,font=('arial',20,'bold'),bg="white",command=lambda:added_value.operation("mod")).grid(row=4,column=5,pady=1)
btnlog2=Button(calc,text="log2",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.log10).grid(row=5,column=5,pady=1)
btnlog10=Button(calc,text="log10",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.log2).grid(row=4,column=6,pady=1)
btnxsq=Button(calc,text="x^2",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.x2).grid(row=1,column=6,pady=1)
btnxcube=Button(calc,text="x^3",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.x3).grid(row=2,column=6,pady=1)
btndeg=Button(calc,text="deg",width=6,height=2,font=('arial',20,'bold'),bg="powder blue",command=added_value.deg).grid(row=5,column=6,pady=1)
lblDisplay=Label(calc,text="Scientific Calculator",font=('arial',20,'bold'),justify=CENTER)
lblDisplay.grid(row=0,column=4,columnspan=4)



#======================================================MENU and Functions=====================================
def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific Calculator","Press yes to exit")
    if(iExit>0):
        root.destroy()
        return


def Scientific():
    root.resizable(width=FALSE, height=False)
    root.geometry("816x568+0+0")


def Standard():
    root.resizable(width=FALSE,height=False)
    root.geometry("480x568+0+0")
menubar=Menu(calc)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Standard",command=Standard)
filemenu.add_command(label="Scientific",command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)


editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")


helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help")





root.config(menu=menubar)
root.mainloop()



