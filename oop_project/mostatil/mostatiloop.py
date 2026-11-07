

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



from yek_mostatatil import mostatil



    
newMastatil=mostatil()
      

# newMastatil=mostatil()
btn1=tkinter.Button(window,text='رسم',command=newMastatil.shapeall)
btn1.grid(row=5,column=1)
btn2=tkinter.Button(window,text='پاک کردن',command=newMastatil.pakkardn)
btn2.grid(row=4,column=1)
window.mainloop()




    