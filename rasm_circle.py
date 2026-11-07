#رسم دایره و مربع
import turtle
t1=turtle.Turtle()
import tkinter
from tkinter import messagebox as msg 
def circle2():
    t1.reset()
    try: 
        num1=int(numEntry1.get())
        tedadshape=int(numEntry2.get())
        
        for i in range(tedadshape):
                    t1.circle(num1)
                    t1.left(360/tedadshape)
    except:
         msg.showerror("لطفا عدد وارد کنید")
         

def moraba():
    t1.reset()
    try:   
            
        num1=int(numEntry1.get())
        tedadshape=int(numEntry2.get())

        for i in range(tedadshape):
                        
                    for i in range(4):
                        t1.forward(num1)
                        t1.left(90)
                    t1.left(360/tedadshape)
    except:  
         msg.showerror("لطفا عدد وارد کنید")  
         
def pakkardan():
     screen1=turtle.Screen()
     screen1.clearscreen()   
         

window=tkinter.Tk()
window.title('برنامه رسم شکل')
tkinter.Label(window,text='اندازه ضلع را وارد کنید').grid(row=0,column=0)
numEntry1=tkinter.Entry(window)
numEntry1.grid(row=0,column=1)
tkinter.Label(window,text='تعداد شکل').grid(row=0, column=3)
numEntry2=tkinter.Entry(window)
numEntry2.grid(row=0,column=4)
btn1=tkinter.Button(window,text='رسم دایره',command=circle2)
btn1.grid(row=1,column=0)

btn2=tkinter.Button(window,text='رسم مربع',command=moraba)
btn2.grid(row=2,column=0)

btn3=tkinter.Button(window,text='پاک کردن ',command=pakkardan)
btn3.grid(row=3,column=1)


window.mainloop()
