from turtle import Turtle

class assign_state(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def assign(self, x_y, state_name):
        self.goto(x_y)
        self.write(f"{state_name}", align="center")

