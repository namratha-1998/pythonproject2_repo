from tkinter import *
class addition:
    def __init__(self,win):
        self.l1=Label(win,text="first number")
        self.l2=Label(win,text="second number")
        self.l3=Label(win,text="result")
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.l1.place(x=100,y=50)
        self.t1.place(x=200,y=50)
        self.l2.place(x=100,y=100)
        self.t2.place(x=200,y=100)
        self.bt1=Button(win,text="add",command=self.add)
        self.bt2=Button(win,text="sub",command=self.sub)
        self.bt3=Button(win,text="mul",command=self.mul)
        self.bt4=Button(win,text="div",command=self.div)
        self.bt1.place(x=100,y=150)
        self.bt2.place(x=200,y=150)
        self.bt3.place(x=300,y=150)
        self.bt4.place(x=400,y=150)
        self.l3.place(x=100,y=200)
        self.t3.place(x=200,y=200)
    def add(self):
        self.t3.delete(0,"end")
        n1=int(self.t1.get())
        n2=int(self.t2.get())
        r=n1+n2
        self.t3.insert(END, str(r))
    def sub(self):
        self.t3.delete(0,"end")
        n1=int(self.t1.get())
        n2=int(self.t2.get())
        r=n1-n2
        self.t3.insert(END, str(r))
    def mul(self):
        self.t3.delete(0,"end")
        n1=int(self.t1.get())
        n2=int(self.t2.get())
        r=n1*n2
        self.t3.insert(END, str(r))
    def div(self):
        self.t3.delete(0,"end")
        n1=int(self.t1.get())
        n2=int(self.t2.get())
        r=n1/n2
        self.t3.insert(END, str(r))
