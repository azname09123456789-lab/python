#طراحي کارت
import tkinter
from tkinter import messagebox as msg
import turtle
t1=turtle.Turtle()
t1.color('blue')
t1.fillcolor('blue')
for i in range(4):
    t1.forward(300)
    t1.left(90)
t1.penup()
t1.goto(220,250)
t1.pendown()
t1.left(180)
t1.write("کيان ",align='right', font=('tahoma', 15))
t1.write(":نام ",font=('tahoma', 20,'bold'))


t1.penup()
t1.goto(100,200)
t1.pendown()
t1.left(180)
t1.write("رحماني",align='right' ,font=('tahoma',15))
t1.write(":نام خانوادگي", font=('tahoma',20,'bold'))
t1.penup()
t1.goto(160,150)
t1.pendown()
t1.left(180)
t1.write("2920891456",align='right',font=('tahoma',15))
t1.write(":کد ملي",font=('tahoma',20,'bold'))

t1.penup()
t1.goto(150,100)
t1.pendown()
t1.left(180)
t1.write("5951636777",align='right',font=('tahoma',15))
t1.write(":کد پستي",font=('tahoma',20,'bold'))



window=tkinter.Tk()
window.title('کارت ملی ')
tkinter.Label(window, text='کارت ملی شما ساخته شد').grid(row=0, column=0)
numEntry1=tkinter.Entry()
msg.showinfo("طراحی کارت انجام شد")
window.mainloop()
    

