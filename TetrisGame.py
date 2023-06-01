import turtle, random

SCALE = 32 #Controls how many pixels wide each grid square is

class Game: 
    '''
Purpose: (What does an object of this class represent?)
draw the board and call a bunch of turtle functions that ensure that the turtle graphics are running as fast as possible, and allows user to move blocks either left or right if coordinates
are within bounds.
Instance variables: (What are the instance variables for this class,
and what does each represent in a few words?)
self, and turtle variables which are used to set board game up. self.occupied, which is used to represent if a square on the board is already
filled up.
Methods: (What methods does this class have, and what does each do in a few words?)
gameloop: where it moves downwards one step every 300 milliseconds, if within bounds.
move_left : moves blocks to the left if users presses left 
move_right : moves blocks to the irght if user presses right.
'''

    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)
        

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)            
        
        self.occupied = []
        for i in range(20):
            newlist= []
            for j in range(10):
                newlist.append(False)
            self.occupied.append(newlist)
            
        self.active = Block()

        #These three lines must always be at the BOTTOM of __init_
        turtle.ontimer(self.gameloop, 300)
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.update()
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        if self.active.valid(0,-1,self.occupied):
            self.active.move(0,-1)
            turtle.update()
        else:
            for i in self.active.squares:
                self.occupied[i.ycor()][i.xcor()] = True
            self.active=Block()
        turtle.ontimer(self.gameloop, 300)
        
    def move_left(self):
        if self.active.valid(-1,0,self.occupied):
            self.active.move(-1,0)
            turtle.update()


    def move_right(self):
        if self.active.valid(1,0,self.occupied):
            self.active.move(1,0)
            turtle.update()







class Square(turtle.Turtle):
    '''
Purpose: (What does an object of this class represent?)
object of this class represents the layout of the board, with the shape being square and color being gray.
Instance variables: (What are the instance variables for this class,
and what does each represent in a few words?)
self,x,y,: x,y represent coordinate points on the square board, color represents color of board squares, 
Methods: (What methods does this class have, and what does each do in a few words?)
no methods.
'''

    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
        self.goto(x,y)

class Block:
    '''
Purpose: (What does an object of this class represent?)
the objects represent how the blocks while playing the game will move and keep it within the bounds of the game block.
Instance variables: (What are the instance variables for this class,
and what does each represent in a few words?)
The instance variables are self.squares, representing a square, a color and a coordinate. Self.occupied is from the game class.
Methods: (What methods does this class have, and what does each do in a few words?)
move= moves and get x and y coordinates.
valid= values representing the change in x or y coordinates to apply to each square.
'''

    def  __init__(self):
            self.squares = []
            options = random.randint(1,7)
            if options == 1:
                self.squares.append(Square(3,20,'cyan'))
                self.squares.append(Square(4,20,'cyan'))
                self.squares.append(Square(5,20,'cyan'))
                self.squares.append(Square(6,20,'cyan'))
            elif options == 2:
                self.squares.append(Square(3,19,'blue'))
                self.squares.append(Square(3,20,'blue'))
                self.squares.append(Square(4,20,'blue'))
                self.squares.append(Square(5,20,'blue'))
            elif options == 3:
                self.squares.append(Square(3,20,'orange'))
                self.squares.append(Square(4,20,'orange'))
                self.squares.append(Square(5,20,'orange'))
                self.squares.append(Square(5,19,'orange'))
            elif options == 4:
                 self.squares.append(Square(3,19,'yellow'))
                 self.squares.append(Square(4,19,'yellow'))
                 self.squares.append(Square(3,20,'yellow'))
                 self.squares.append(Square(4,20,'yellow'))
            elif options == 5:
                 self.squares.append(Square(3,20,'green'))
                 self.squares.append(Square(4,20,'green'))
                 self.squares.append(Square(4,19,'green'))
                 self.squares.append(Square(5,19,'green'))
            elif options == 6:
                 self.squares.append(Square(3,20,'purple'))
                 self.squares.append(Square(4,20,'purple'))
                 self.squares.append(Square(5,20,'purple'))
                 self.squares.append(Square(4,19,'purple'))
            else:
                self.squares.append(Square(3,19,'red'))
                self.squares.append(Square(4,19,'red'))
                self.squares.append(Square(4,20,'red'))
                self.squares.append(Square(5,20,'red'))

    def move(self,dx,dy):
        for i in self.squares:
            i.goto(i.xcor()+dx,i.ycor()+dy)
    def valid(self, dx, dy,occupied):
        for i in self.squares:
            if i.xcor()+dx < 0. or i.xcor()+dx > 9 or i.ycor()+dy < 0:
                return False
            if occupied[i.ycor()+dy][i.xcor()+dx] == True:
                return False
        return True


    




if __name__ == '__main__':
    Game()