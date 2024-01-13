from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.points = 0
        with open("high_score.txt", mode="r") as hs:
            self.Highscore = hs.read()
        
    def score(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.write(f"Score: {self.points}, HighScore: {self.Highscore}", align="center", font=("courier", 14, "normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("Game Over!!!", align="center", font=("courier", 18, "normal"))


    def reset_score(self):
        if self.points>int(self.Highscore):
            self.Highscore = self.points
            with open('high_score.txt', mode="w") as hs:
                hs.write(str(self.Highscore))
        self.points = 0
        self.score()


