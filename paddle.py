from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        self.position = position
        super().__init__("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_left(self, event):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def size_half(self):
        self.shapesize(stretch_wid=1, stretch_len=2.5)

    def move_right(self, event):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def restart(self):
        self.goto(self.position)

    def move_cursor(self, event):
        x = event.x - 400
        self.goto(x, self.ycor())
