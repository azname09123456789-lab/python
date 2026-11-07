#برنامه برسي زوج يا فرد بودن يک عدد
import tkinter
from tkinter import messagebox as msg 

def checknumber():
    try:
            num1=int(numEntry1.get())
        # num1=int(input("لطفا عدد را درج نماييد"))
            if num1%2==0:
                msg.showinfo(title='نتیجه',message=f"عدد {num1}زوج است ")
            else:
                msg.showinfo(title='نتیجه',message=f"عدد {num1} فرد است")
    except:
         msg.showerror(title='اخطار',message=f"لطفا در وارد کردن عدد دقت مبذول فرمایید")

window=tkinter.Tk()
window.title('برسی زوج یا فرد بودن عدد ')
tkinter.Label(window,text='عدد را وارد کنید').grid(row=0,column=0)
numEntry1=tkinter.Entry()
numEntry1.grid(row=0,column=1)
btn1=tkinter.Button(window,text='اجرا',command=checknumber)
btn1.grid(row=1,column=0)


window.mainloop()