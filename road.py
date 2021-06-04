from turtle import Turtle


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.pensize(width=15)
        self.color("white")
        # self.penup()
        # self.hideturtle()

    def draw_middle_line(self):
        self.goto(-320, 0)
        self.forward(620)

        # turtle = Turtle()
        # turtle.pensize(width=5)
        # turtle.penup()
        # turtle.hideturtle()
        # turtle.goto(-320, 0)
        # for _ in range(15):
        #     turtle.forward(20)
        #     turtle.penup()
        #     turtle.forward(20)
        #     turtle.pendown()
