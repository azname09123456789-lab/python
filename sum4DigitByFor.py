#برنامه حاصل ضرب اعداد با for
def math2():
    try:
        tedad=int(input("لطفا تعاد اعدادي  که ميخواهيد ضرب شود را درج نماييد"))
        sum1=1
        for i in range(1,tedad+1):
            num1=float(input(f"عدد {i} را درج نماييد"))
            sum1=sum1*num1
        print(f"حاصل ضرب اين {tedad} برابر است با {sum1}")
    except:
           print(f"در وارد کردن کد دقت مبذول فرماييد")
        
