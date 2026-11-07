#برنامه عمليات رياضي
#def math1(num1:float,num2:float,num3:float,num4:float):
def math1():
    try:
        num1=float(input("لطفا عدد اول را درج نماييد"))
        num2=float(input("لطفا عدد دوم را درج نماييد"))
        num3=float(input("لطفا عدد سوم را درج نماييد"))
        num4=float(input("لطفا عدد چهارم را درج نماييد"))
        num5=num1+num2+num3+num4
        print(f"حاصل جمع چهار عدد {num1}و{num2}و{num3}و {num4}برابر است با{num5}")
    except:
        print("در وارد کردن کد دقت مبذول فرماييد")
