from turtle import Turtle

INITIAL_LENGTH = 3
INITIAL_SPEED = 0.3
SEGMENT_SIZE = 20
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
X_LIMIT = 280
Y_LIMIT = 280


class Snake:
    def __init__(self):
        self.length = INITIAL_LENGTH
        self.speed = INITIAL_SPEED
        self.segments = []
        self.create_segments()

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("greenyellow")
        new_segment.pencolor("black")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_segments(self):
        for segment_id in range(0, self.length):
            seg_loc = (0, -SEGMENT_SIZE * segment_id)
            self.add_segment(seg_loc)

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.length += 1
        self.speed *= 0.95

    def move(self):
        for segment_id in range(self.length - 1, -1, -1):
            if segment_id == 0:
                self.segments[segment_id].forward(MOVE_DISTANCE)
            else:
                target_coordinates = self.segments[segment_id - 1].pos()
                self.segments[segment_id].goto(target_coordinates)

    def face_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def face_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def face_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def face_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def is_out_of_bounds(self):
        head_x_coord = self.segments[0].pos()[0]
        head_y_coord = self.segments[0].pos()[1]
        is_oob = abs(head_x_coord) > X_LIMIT or abs(head_y_coord) > Y_LIMIT
        return is_oob

    def is_colliding_with_self(self):
        for segment_index in range(1, self.length):
            distance_to_head = self.segments[segment_index].distance(self.segments[0])
            #print(distance_to_head)
            if distance_to_head < 10:
                return True
        return False
