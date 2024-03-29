from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=620, width=640)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
  screen.update()
  time.sleep(0.15)
  scoreboard.score()
  if snake.segments[0].distance(food) <  15:
    scoreboard.points+=1
    food.refresh()
    snake.grow()
    scoreboard.score()
#snake going out of board
  if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
    snake.reset()
    scoreboard.reset_score()
# Tail collision
  for seg in snake.segments[1:]:
    if snake.segments[0].distance(seg) < 10:
      snake.reset()
      scoreboard.reset_score()

  snake.move()
  


screen.exitonclick()