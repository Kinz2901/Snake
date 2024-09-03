from turtle import Screen, Turtle
from snake import Snake
import random

class Fruit(Turtle):
  def __init__(self, segments):
    self.segments = segments
    Turtle.__init__(self)
    self.shape("circle")
    self.shapesize(0.7)
    self.color("blue")
    self.penup()
    self.speed("fastest")
    self.comeu()
    



  def comeu(self):
    for segment in self.segments:
      while segment.distance(self) < 15:
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)

