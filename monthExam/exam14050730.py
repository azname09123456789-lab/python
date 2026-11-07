import tkinter
from tkinter import messagebox as msg
import random

#def reshte_tasadofi():
    #reshte="abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    #for i in range(reshte):
        #place1=random.randint(0,len(reshte)-1)
reshte="abcdefghijklmnopqrstuvwxwzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def tolid_tasodafi():
        length1= int(tolreshte.get().strip())
        for i in range(length1):
            place =random.randint(0,len(reshte)-1)
            random_charecter=reshte[place]
            print(random_charecter, end='')
    
        
                 

def tolid_otomatik():
   length= int(tolreshte.get())
   for j in range(100):
         for i in range(length):
             place1 = random.randint(0, len(reshte) - 1)
             place += reshte[place1]
                     




            

window=tkinter.Tk()
window.title('رسم شکل')  
tkinter.Label(window,text='لطفا طول رشته را درج درج نمایید').grid (row=0,column=0)
tolreshte=tkinter.Entry(window)
tolreshte.grid(row=0,column=1)

btn=tkinter.Button(window,text='تولید تصادفی',command=tolid_tasodafi)
btn.grid(row=0,column=2)
btn1=tkinter.Button(window,text='تولید اتوماتیک',command=tolid_otomatik)
btn1.grid(row=1,column=2)





window.mainloop()