
import turtle
t1=turtle.Turtle()
class mostatil: 
    def __init__(self):
        pass
        #self.tedadshape =(numEntrytedadshape.get().strip())
        #self.andazeh = (numEntryandazezel.get().strip())
        #self.tedadzel = (numEntryandazezel.get().strip())
    def get_masahat(self):
            
        s=self.andazeh*self.andazeh
        return s
    def get_mohit(self):
        p=(self.andazeh+self.andazeh)*2
        return  p
    def shapeOne(self,t1):
        t1.forward(self.andazeh)
        t1.left(90)
        t1.forward(self.andazeh)
        t1.left(90)
        t1.forward(self.andazeh)
        t1.left(90)
        t1.forward(self.andazeh)
    def shapeall(self):
        import turtle
        t1=turtle.Turtle()

        self.tedadshape =int(numEntrytedadshape.get().strip())
        self.andazeh = int(numEntryandazezel.get().strip())
        self.tedadzel = int(numEntrytedadzel.get().strip())
        
        tedad=self.tedadshape
        andazeh=self.andazeh
        tedadzel=self.tedadzel
        msg.showinfo(title='نتیجه', message=f'{tedad}تعداد برابر است با:  ')

        for i in range(tedad):
            t1.left(360/tedad)
            for j in range(tedadzel):
                t1.forward(andazeh)
                t1.left(360/tedadzel)
    def pakkardn():
     screen1=turtle.Screen()
     screen1.clearscreen()
