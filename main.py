from turtle import Screen
import time
from snake import Snake
from fruit import Fruit
from score import Score
from game_over import GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
fruit = Fruit(snake.segments)
score = Score()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  headpositionx = int(snake.segments[0].xcor())
  headpositiony = int(snake.segments[0].ycor())
  snake.move()
  if snake.head.distance(fruit) < 15:
    fruit.comeu()
    snake.extend()
    score.increase_score()
  elif headpositionx > 280 or headpositiony > 280 or headpositionx < -280 or headpositiony < -280 :
    game_is_on = False
    GameOver()

  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      GameOver()

screen.exitonclick()

