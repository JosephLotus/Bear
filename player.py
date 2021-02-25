from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def up_turtle(self):
        self.forward(MOVE_DISTANCE)

    def down_turtle(self):
        self.backward(MOVE_DISTANCE)

    def left_turtle(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def right_turtle(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def reset_pos(self):
        self.goto(STARTING_POSITION)
