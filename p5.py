#برنامه برسي کد ملي
import tkinter
from tkinter import messagebox as msg
def checkmeli():
    num1 = numEntry1.get()
    try:
       # num1=(input("لطفا کد ملي را درج نماييد "))
        if len(num1)==10:
          num1=int(num1)
          yekan=num1%10
          if yekan==0 or yekan==1:
            msg.showinfo(title='نتیجه', message=f"لطقا در روز شنبه مراجعه کنید")
          if yekan==2 or yekan==3 or yekan==4:
            msg.showinfo(title='نتیجه', message=f"لطفا روز يک شنبه يا دوشنبه  مراجعه کنيد")
          if yekan==5 or yekan==6:
            msg. showinfo(title='نتیجه', message=f"لطفا روز سه شنبه مراجعه کنید ")
          if yekan==7:
            msg. showinfo(title='نتیجه', message=f"لطفا روز چهاشنبه مراجعه کنید")
          if yekan==8 or yekan==9:
            msg. showinfo(title='نتیجه', message=f"لطفا روز پنج شنبه مراجعه کنید")
        else:
         msg.showerror(title='خطا',message="کد ملي بايد 10 رقمي باشد")
    except:
            msg.showerror(title='خطا',message="لطفا عدد وارد نماييد")
window=tkinter.Tk()
window.title('برنامه محاسبه کد ملی')
tkinter.Label(window,text='کد ملی')
numEntry1=tkinter.Entry()
numEntry1.grid(row=0,column=0)
btn1=tkinter.Button(text='اجرا',command=checkmeli)
btn1.grid(row=1,column=0)



window.mainloop()