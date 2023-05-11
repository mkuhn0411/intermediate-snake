from turtle import Turtle
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle("square")
        segment.up()
        segment.color("green")
        segment.goto(position)
        self.segments.append(segment)

    def create_snake(self):
        for index in range(0, 3):
            position = index * (move_distance * -1), 0
            self.add_segment(position)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        self.head.heading() != DOWN and self.head.setheading(UP)

    def down(self):
        self.head.heading() != UP and self.head.setheading(DOWN)

    def left(self):
        self.head.heading() != RIGHT and self.head.setheading(LEFT)

    def right(self):
        self.head.heading() != LEFT and self.head.setheading(RIGHT)

    def move_segments(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_coors = (self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
            self.segments[seg_num].goto(new_coors)

        self.head.forward(move_distance)




