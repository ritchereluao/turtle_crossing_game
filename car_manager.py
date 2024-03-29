from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_right_cars = []
        self.all_left_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_right_car(self):
        random_chance = random.randint(1, 8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # random_y = random.randint(-250, 250)
            random_y = random.randint(20, 230)
            new_car.goto(300, random_y)
            self.all_right_cars.append(new_car)

    def create_left_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_left_car = Turtle("square")
            new_left_car.shapesize(stretch_wid=1, stretch_len=2)
            new_left_car.penup()
            new_left_car.color(random.choice(COLORS))
            random_y = random.randint(-230, -10)
            new_left_car.goto(-300, random_y)
            self.all_left_cars.append(new_left_car)

    def move_cars(self):
        for car in self.all_right_cars:
            car.backward(self.car_speed)
        for car in self.all_left_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
