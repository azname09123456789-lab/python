import tkinter as tk
class rectangle:
    def __init__(self):
        self.numOne=num1.get().strip()
        pass


window1=tk.Tk()
window1.title('بررسی ارسال متغییر')

num1=tk.Entry(window1)
num1.pack()

window1.mainloop()
newRect=rectangle()