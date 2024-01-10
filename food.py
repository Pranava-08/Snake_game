from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color('white', 'green')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        FOOD_POS = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(FOOD_POS)
