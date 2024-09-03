from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class GameOver(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.write(f"Game Over.", align=ALIGNMENT, font=FONT)
