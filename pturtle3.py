import turtle
import random

tedadShape=int(input("لطفا تعداد شکلي که ميخواهيد چاپ شود را درج نماييد"))
tedad=int(input("لطفا ضلع را درج نماييد "))
num2=int(input("لطفا اندازه ضلع را درج نماييد "))
#psize=int(input("لطفا اندازه ضخامت ضلع را درج نماييد "))
spee=int(input("لطفا سرعت رسم را درج نماييد"))
listColor=list()
listColor=["red","green","black","blue", "brown","orange","purple","yellow","pink","gray","white"]
t1=turtle.Turtle()
#t1.pensize(psize)

degre=360/tedad
t1.speed(spee)
for i in range(tedadShape):
    t1.left(360/tedadShape)
    colorIndex=random.randint(0,len(listColor)-1)
    colorIndex2=random.randint(0,len(listColor)-1)
    pensize=random.randint(1,10)
    t1.pensize(pensize)
    #num2=random.randint(1,90)
    
    #t1.fillcolor(listColor[colorIndex])
    t1.color(listColor[colorIndex2])
    #t1.begin_fill()
    for i in range (1,tedad+1):
        pensise=random.randint(1,10)
        t1.pensize(pensise)
        colorIndex=random.randint(0,len(listColor)-1)
        color=listColor[colorIndex]
        t1.color(color)
        t1.forward(num2)
        t1.left(degre)
    t1.end_fill()
   
