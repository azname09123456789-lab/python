#برنامه عمليات رياضي
import tkinter
from tkinter import messagebox as msg
# tk=tkinter.Tk()
def func1():
        try:
                 num1=int(numEntry1.get().strip())
                 num2=int(numEntry2.get().strip())

                 num3=num1+num2

                 msg.showinfo(title='نتیجه', message=f'حاصل جمع دو عدد {num1} و {num2} برابر است با:   {num3}')
        except:
                msg.showinfo(title='نتیجه', message=f'لطفا در وارد کردن عدد دقت مبذول فرمایید')

def func2():
        try:
              num4=int(numEntry1.get().strip())
              num5=int(numEntry2.get().strip())

              num6=num5-num4

              msg.showinfo(title='نتیجه', message=f'حاصل تفریق دوعدد {num4}و  {num5}برابر است با :   {num6}')
        except:
                msg.showerror(title='نتیجه', message=f'لطفا در وارد کردن عدد دقت مبذول فرمایید')

def func3():
        try:
                num7=int(numEntry1.get().strip())
                num8=int(numEntry2.get().strip())
                
                num9=num8*num7
        
                msg.showinfo(title='نتیجه', message=f'حاصل ضرب دو عدد {num7} و {num8} برابر است با :{num9}')
        except:
                msg.showerror(title='نتیجه', message=f'لطفا در وارد کردن عدد دقت مبذول فرمایید')

def func4():
    try:
           num10=int(numEntry1.get().strip())
           num11=int(numEntry2.get().strip())
            
           num12=num10/num11 
           msg.showinfo(title='نتیجه', message=f'حاصل تقسیم دو عدد {num10} و {num11}برابر است با :{num12}')
    except:
           msg.showerror(title='نتیجه', message=f'لطفا در وارد کردن عدد دقت مبذول فرمایید')
    #     num1=float(input("لطفا عدد اول را درج نماييد "))
    #     num2=float(input("لطفا عدد دوم را درج نماييد "))
    #     num3=num1+num2
    #     num4=num1-num2
    #     num5=num1*num2
    #     num6=num1/num2
    #     print(f"حاصل جمع دو عدد {num1} و {num2} برابر است با:  {num3}")
    #     print(f"حاصل تفريق دو عدد {num1}و {num2}برابر است با:  {num4}")
    #     print(f"حاصل ضرب دوعدد {num1}و {num2}برابر است با:  {num5}")
    #     print(f"حاصل تقسيم دو عدد {num1}و{num2}برابر است با  {num6}")
    # except:
    #     print("در وارد کردن کد دقت مبذول فرماييد")

window=tkinter.Tk()
window.title('برنامه بررسی عملیات ریاضی بر روی دو عدد')
tkinter.Label(window, text='عدد اول').grid(row=0, column=1)
numEntry1=tkinter.Entry()
numEntry1.grid(row=0, column=0)
tkinter.Label(window, text='عدد دوم').grid(row=1, column=1)
numEntry2=tkinter.Entry()
numEntry2.grid(row=1, column=0)

btn1=tkinter.Button(text='+', command=func1)
btn1.grid(row=2, column=0)
btn2=tkinter.Button(text='-', command=func2)
btn2.grid(row=2, column=1)
btn3=tkinter.Button(text='*', command=func3)
btn3.grid(row=2, column=2)
btn4=tkinter.Button(text='/', command=func4)
btn4.grid(row=2, column=3)









window.mainloop()