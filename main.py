from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.tracer(0)
t=Snake()
f=Food()
ss=Score()
s.listen()
s.onkey(t.upp,"Up")
s.onkey(t.down,"Down")
s.onkey(t.turnright,"Right")
s.onkey(t.turnleft,"Left")

gameison=True
while gameison:
    s.update()
    time.sleep(0.1)
    t.move()
    if t.segments[0].distance(f)<15:
        f.refresh()
        ss.increase()
        t.extend()
    #collisions
    #1.ends
    if t.segments[0].xcor()>280 or t.segments[0].xcor()<-280 or t.segments[0].ycor()>280 or t.segments[0].ycor()<-280:
        gameison = False
        ss.gameover()
    #2.own body
    for segg in t.segments[1:]:
        if t.segments[0].distance(segg)<15:
            gameison = False
            ss.gameover()



s.exitonclick()