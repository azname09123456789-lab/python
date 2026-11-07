import turtle
tedad=int(input("لطفا ضلع را درج نماييد "))
num2=int(input("لطفا اندازه ضلع را درج نماييد "))
psize=int(input("لطفا اندازه ضخامت ضلع را درج نماييد "))
spee=int(input("لطفا سرعت رسم را درج نماييد"))
t1=turtle.Turtle()
t1.pensize(psize)
t1.color('blue')
t1.fillcolor("green")
t1.begin_fill()
degre=360/tedad
t1.speed(spee)
for i in range (1,tedad+1):
    t1.forward(num2)
    t1.left(degre)
t1.end_fill()
   
