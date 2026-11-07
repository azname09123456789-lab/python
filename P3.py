#برنامه عمليات رياضي
def math1(num1:float,num2:float,num3:float,num4:float):
    try:
       # num1=float(input("لطفا عدد اول را درج نماييد"))
       # num2=float(input("لطفا عدد دوم را درج نماييد"))
       # num3=float(input("لطفا عدد سوم را درج نماييد"))
        num4=num1+num2+num3
        num5=num1-num2-num3
        num6=num1*num2*num3
        num7=num1/num2/num3
        print(f"حاصل جمع سه عدد  {num1}و{num2}و{num3}برابر است با :{num4}")
        print(f"حاصل تفريق سه عدد {num1}و{num2}و{num3}برابر است با:{num5}")
        print(f"حاصل ضرب سه عدد {num1}و{num2}و{num3}برابر است با:{num6}")
        print(f"حاصل تقسيم سه عدد{num1}و{num2}و{num3}برابر است با :{num7}")
    except:
        print("در وارد کردن کد دقت مبذول فرماييد")
