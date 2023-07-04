from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_segment(position)

    def add_segment(self,position):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.turtles.append(turtle)

    def extend(self):
        self.add_segment(self.turtles[-1].position())


    def move(self):
        # Move the snake by updating the positions of each segment
        for turt_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turt_num - 1].xcor()
            new_y = self.turtles[turt_num - 1].ycor()
            self.turtles[turt_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Change the snake's direction to up, if it's not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the snake's direction to down, if it's not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the snake's direction to left, if it's not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the snake's direction to right, if it's not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
