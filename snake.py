from turtle import Turtle
start_Pos = [(0,0), (-20,0), (-40,0)]
move_dist = 20
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in start_Pos:
            self.add_seg(pos)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()


    def add_seg(self, pos):
        new_seg = Turtle("square")
        new_seg.color("White")
        new_seg.penup()
        #new_seg.shapesize(stretch_len=1.5, stretch_wid=1.5)
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def grow(self):
        self.add_seg(self.segments[-1].pos())

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.segments[0].forward(move_dist)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

