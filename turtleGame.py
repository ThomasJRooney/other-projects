# Thomas Rooney roone194

# I understand this is a graded, individual examination that may not be
# discussed with anyone.  I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

#Completed through Task 8

from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

class LaserBeam(RawTurtle):
    def __init__(self, canvas, x, y, direction, dx, dy):
        super().__init__(canvas)
        self.penup()
        self.goto(x,y)
        self.setheading(direction)
        self.color("Green")
        self.lifespan = 200
        xPrime = math.cos(math.radians(direction))
        yPrime = math.sin(math.radians(direction))
        self.__dx = xPrime * 2 + dx
        self.__dy = yPrime * 2 + dy
        self.shape("laser")

    #Accessors/Getters
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def get_lifespan(self):
        return self.lifespan

    def getRadius(self):
        return 4

    #moving laser
    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()
        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        self.goto(x,y)
        self.lifespan -= 1


class Ghost(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y,size):
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        if self.__size==3:
            self.shape("blueghost.gif")
        elif self.__size==2:
            self.shape("pinkghost.gif")

    #Moves the ghost from its current position to a new position
    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()
        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        self.goto(x,y)

    #returns the apprximate "radius" of the Ghost object
    def getRadius(self):
        return self.__size * 10 - 5

    #Mutators/setters
    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    #Accessors/getters
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

class FlyingTurtle(RawTurtle):
    def __init__(self,canvasobj,dx,dy,x,y,size):
        RawTurtle.__init__(self,canvasobj)
        self.penup()
        self.color("purple")
        self.goto(x,y)
        self.__dx = dx
        self.__dy = dy
        self.__size = size
        self.shape("turtle")

    def move(self):
        screen = self.getscreen()
        x = self.xcor()
        y = self.ycor()
        x = (self.__dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
        y = (self.__dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
        self.goto(x,y)

    def turboBoost(self):
        angle = self.heading()
        x = math.cos(math.radians(angle))
        y = math.sin(math.radians(angle))
        self.__dx = self.__dx + x
        self.__dy = self.__dy + y

    def stopTurtle(self):
        angle = self.heading()
        self.__dx = 0
        self.__dy = 0

    def getRadius(self):
        return 2

    #Mutators/setters
    def set_dx(self, dx):
        self.__dx = dx

    def set_dy(self, dy):
        self.__dy = dy

    #Accessors/getters
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

def intersect(obj1, obj2):
    rad1 = obj1.getRadius()
    rad2 = obj2.getRadius()
    radAdd = rad1 + rad2
    distance = math.sqrt((obj1.xcor() - obj2.xcor()) ** 2 + (obj1.ycor() - obj2.ycor()) ** 2)
    if distance <= radAdd:
        return True
    else:
        return False

def main():

    # Start by creating a RawTurtle object for the window.
    firstwindow = tkinter.Tk()
    firstwindow.title("Turtle Saves the World!")
    canvas = ScrolledCanvas(firstwindow,600,600,600,600)
    canvas.pack(side = tkinter.LEFT)
    t = RawTurtle(canvas)

    screen = t.getscreen()
    screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)
    screen.register_shape("blueghost.gif")
    screen.register_shape("pinkghost.gif")
    screen.register_shape("laser",((-2,-4),(-2,4),(2,4),(2,-4)))
    frame = tkinter.Frame(firstwindow)
    frame.pack(side = tkinter.RIGHT,fill=tkinter.BOTH)
    scoreVal = tkinter.StringVar()
    scoreVal.set("0")
    scoreTitle = tkinter.Label(frame,text="Score")
    scoreTitle.pack()
    scoreFrame = tkinter.Frame(frame,height=2, bd=1,
    relief=tkinter.SUNKEN)
    scoreFrame.pack()
    score = tkinter.Label(scoreFrame,height=2,width=20,textvariable=scoreVal, fg= 'Yellow',bg= "black")
    score.pack()
    livesTitle = tkinter.Label(frame, text="Extra Lives Remaining")
    livesTitle.pack()
    livesFrame = tkinter.Frame(frame,height=30,width=60,relief=tkinter.SUNKEN)
    livesFrame.pack()
    livesCanvas = ScrolledCanvas(livesFrame,150,40,150,40)
    livesCanvas.pack()
    livesTurtle = RawTurtle(livesCanvas)
    livesTurtle.ht()
    livesScreen = livesTurtle.getscreen()
    life1 = FlyingTurtle(livesCanvas,0,0,-35,0,0)
    life2 = FlyingTurtle(livesCanvas,0,0,0,0,0)
    life3 = FlyingTurtle(livesCanvas,0,0,35,0,0)
    lives = [life1, life2, life3]
    t.ht()

    screen.tracer(10)

    #Tiny Turtle!
    flyingturtle = FlyingTurtle(canvas,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY,3)

    #A list to keep track of all the lasers
    lasers = []

    def fireLaser():
        ftdx = flyingturtle.get_dx()
        ftdy = flyingturtle.get_dy()
        laser = LaserBeam(canvas, flyingturtle.xcor(), flyingturtle.ycor(), flyingturtle.heading(), ftdx, ftdy)
        lasers.append(laser)

    #A list to keep track of all the ghosts
    ghosts = []

    #Create some ghosts and randomly place them around the screen
    for numofghosts in range(6):
        dx = random.random()*6  - 4
        dy = random.random()*6  - 4
        x = random.random() * (screenMaxX - screenMinX) + screenMinX
        y = random.random() * (screenMaxY - screenMinY) + screenMinY

        ghost = Ghost(canvas,dx,dy,x,y,3)

        ghosts.append(ghost)

        deadLasers = []

        hitGhosts = []

        tinyGhostCollision = []

    def play():
        #start counting time for the play function
        ##LEAVE THIS AT BEGINNING OF play()
        start = datetime.datetime.now()

        if len(hitGhosts) == 6:
            tkinter.messagebox.showinfo("You Win!!", "You saved the world!")
            return

        if len(tinyGhostCollision) == 3:
            tkinter.messagebox.showinfo("You Lose!!", "You didn't save the world!")
            return

        for each_ghost in ghosts:
            if intersect(flyingturtle, each_ghost):
                tkinter.messagebox.showwarning( "Uh-Oh","You Lost a Life!")
                each_ghost.ht()
                each_ghost.goto(each_ghost.xcor() + 75, each_ghost.ycor() + 75)
                each_ghost.st()
                tinyGhostCollision.append(each_ghost)
                life = lives.pop()
                life.ht()

        # Move the turtle
        flyingturtle.move()

        for laser in lasers:
            if laser.lifespan > 0:
                laser.move()
            else:
                laser.goto(-screenMinX * 2, -screenMinY * 2)
                deadLasers.append(laser)
                lasers.remove(laser)
                laser.ht()

        #Move the ghosts
        for each_ghost in ghosts:
            each_ghost.move()

        for each_ghost in ghosts:
            for each_laser in lasers:
                if intersect(each_ghost, each_laser):
                    lasers.remove(each_laser)
                    deadLasers.append(each_laser)
                    each_laser.goto(-screenMinX * 2, -screenMinY * 2)
                    each_laser.ht()
                    ghosts.remove(each_ghost)
                    hitGhosts.append(each_ghost)
                    each_ghost.goto(-screenMinX * 2, -screenMinY * 2)
                    each_ghost.ht()

        theScore = len(hitGhosts) * 20
        scoreVal.set(str(theScore))

        #stop counting time for the play function
        ##LEAVE THIS AT END OF ALL CODE IN play()
        end = datetime.datetime.now()
        duration = end - start

        millis = duration.microseconds / 1000.0

        # Set the timer to go off again
        screen.ontimer(play,int(10-millis))


    # Set the timer to go off the first time in 5 milliseconds
    screen.ontimer(play, 5)

    #Turn turtle 7 degrees to the left
    def turnLeft():
        flyingturtle.setheading(flyingturtle.heading()+20)

    def turnRight():
        flyingturtle.setheading(flyingturtle.heading()-20)

    #turboBoost turtle
    def forward():
        flyingturtle.turboBoost()

    #stop Turtle
    def stop():
        flyingturtle.stopTurtle()

    #Call functions above when pressing relevant keys
    screen.onkeypress(turnLeft,"Left")
    screen.onkeypress(turnRight, "Right")
    screen.onkeypress(forward,"Up")
    screen.onkeypress(stop, "Down")
    screen.onkeypress(fireLaser, "space")

    screen.listen()
    tkinter.mainloop()

if __name__ == "__main__":
    main()
