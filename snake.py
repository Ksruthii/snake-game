from turtle import Turtle,Screen

#t=Turtle()

startpos=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for pos in startpos:
            self.addseg(pos)

    def addseg(self,pos):
        neew = Turtle("square")
        neew.color("white")
        neew.up()
        # new.shapesize(0.5, 0.5)
        neew.goto(pos)
        self.segments.append(neew)
    def extend(self):
        self.addseg(self.segments[-1].position())

    def move(self):

        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(20)

    def turnright(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def turnleft(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def upp(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

