import time
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[segment_number - 1].xcor()
            next_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        self.head.left(90)

    def right(self):
        self.head.right(90)

    def reset(self):
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    """death animation"""
    def death(self):
        for segment in self.segments:
            segment.color("red")
    """getting rid of the snake's corpse"""
    def clear(self):
        for segment in self.segments:
            segment.reset()





