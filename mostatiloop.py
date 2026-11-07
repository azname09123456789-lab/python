

import tkinter
from tkinter import messagebox as msg
import turtle

window=tkinter.Tk()
window.title('رسم شکل')  
tkinter.Label(window,text='لطفا تعداد شکلی که میخواهید چاپ شود را درج نمایید ').grid (row=0,column=0)
numEntrytedadshape=tkinter.Entry(window)
numEntrytedadshape.grid(row=0,column=1)
tkinter.Label(window,text='لطفا اندازه ضلع را وارد نمایید').grid(row=2,column=0)
numEntryandazezel=tkinter.Entry(window)
numEntryandazezel.grid(row=2,column=1) 
tkinter.Label(window,text='لطفا تعداد ضلع را وارد نمایید ').grid(row=3,column=0)
numEntrytedadzel=tkinter.Entry(window)
numEntrytedadzel.grid(row=3,column=1) 







class mostatil:
    def __init__(self):
        pass
        # self.tedadshape =(numEntrytedadshape.get().strip())
        # self.andazeh = (numEntryandazezel.get().strip())
        # self.tedadzel = (numEntryandazezel.get().strip())
    def get_masahat(self):
            
        s=self.andazeh*self.andazeh
        return s
    def get_mohit(self):
        p=(self.andazeh+self.andazeh)*2
        return  p
    def shapeOne(self,t1):
        t1.forward(self.andazeh)
        t1.left(90)
        t1.forward(self.andazeh)
        t1.left(90)
        t1.forward(self.andazeh)
        t1.left(90)
        t1.forward(self.andazeh)
    def shapeall(self):
        import turtle
        t1=turtle.Turtle()

        self.tedadshape =int(numEntrytedadshape.get().strip())
        self.andazeh = int(numEntryandazezel.get().strip())
        self.tedadzel = int(numEntrytedadzel.get().strip())
        
        tedad=self.tedadshape
        andazeh=self.andazeh
        tedadzel=self.tedadzel
        msg.showinfo(title='نتیجه', message=f'{tedad}تعداد برابر است با:  ')

        for i in range(tedad):
            t1.left(360/tedad)
            for j in range(tedadzel):
                t1.forward(andazeh)
                t1.left(360/tedadzel)
    def pakkardn():
     screen1=turtle.Screen()
     screen1.clearscreen()
    
newMastatil=mostatil()
      
# tol=float(input("لطفاً طول را وارد کنید: "))
# arz= float(input("لطف‌ها عرض را وارد کنید: "))

# s=newMastatil.get_masahat()
# p=newMastatil.get_mohit()
# print(f'masahat mostatil ba tol {tol}, arz {arz} barbaast ba: {s}')  
# print(f'mohit mostatil ba tol {tol}, arz {arz} barbaast ba: {p}')  
# newMastatil.shapeOne()
# newMastatil.shapeall()

# newMastatil=mostatil()
btn1=tkinter.Button(window,text='رسم',command=newMastatil.shapeall)
btn1.grid(row=5,column=1)
btn2=tkinter.Button(window,text='پاک کردن',command=newMastatil.pakkardn)
btn2.grid(row=4,column=1)
window.mainloop()




    