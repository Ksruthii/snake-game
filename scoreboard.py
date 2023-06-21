from turtle import Turtle,Screen
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.up()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score : {self.score}",move=False,align="center",font=("Arial",28,"normal"))
        self.hideturtle()
    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="center", font=("Arial", 28, "normal"))
    def gameover(self):
        self.goto(0,0)
        self.write("game over", move=False, align="center", font=("Arial", 20, "normal"))