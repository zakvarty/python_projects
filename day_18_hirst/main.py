import random as rd
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.fillcolor("AliceBlue")

# Task 1: Draw a square ----
def draw_regular_polygon(n_sides, side_length):
    """
    Draws a regular polygon starting at current location.
    :rtype: null
    """
    for _ in range(n_sides):
        timmy.forward(side_length)
        timmy.left(360 / n_sides)
#draw_regular_polygon(4, 100)


# Task 2: draw a dashed line ----
def draw_dashed_line(total_length, dash_length, gap_length):
    length_remaining = total_length
    print(f"A: {length_remaining}")
    n_full_dashes = total_length // (dash_length + gap_length)
    print(n_full_dashes)
    for _ in range(n_full_dashes):
        timmy.pendown()
        timmy.forward(dash_length)
        timmy.penup()
        timmy.forward(gap_length)
    # Draw partial final dash-gap, ending with pen up at total_length
    length_remaining -= n_full_dashes * (dash_length + gap_length)
    print(f"B: {length_remaining}")
    if length_remaining <= dash_length:
        timmy.pendown()
        timmy.forward(length_remaining)
        timmy.penup()
        length_remaining -= length_remaining
        print(f"C: {length_remaining}")
    else:
        timmy.pendown()
        timmy.forward(dash_length)
        timmy.penup()
        length_remaining -= dash_length
        print(f"D: {length_remaining}")
        timmy.forward(length_remaining)
        length_remaining -= length_remaining
        print(f"A: {length_remaining}")

#draw_dashed_line(100, 10, 5)

# Task 3: drawing nested shapes in random colours ----

# for sides in range(3,11):
#     rgb_tup = (rd.random(), rd.random(), rd.random())
#     timmy.pencolor(rgb_tup)
#     draw_regular_polygon(sides, 70)

# Task 4: Generating a random Manhattan walk ----
def draw_manhattan_random_walk(n_steps, step_length, line_weight):
    timmy.speed(8)
    timmy.hideturtle()
    timmy.pensize(line_weight)
    timmy.pendown()
    for _ in range(n_steps):
        rgb_tup = (rd.random(), rd.random(), rd.random())
        rotation_amount = rd.randrange(0, 4) * 90
        timmy.pencolor(rgb_tup)
        timmy.right(rotation_amount)
        timmy.forward(step_length)
    timmy.speed(6)
    timmy.penup()
    timmy.showturtle()

#draw_manhattan_random_walk(200, 35, 5)

# Task 5: Draw a spirograph
n_circles = 100
timmy.pendown()
timmy.speed(0)
for _ in range(n_circles):
    rgb_tup = (rd.random(), rd.random(), rd.random())
    timmy.pencolor(rgb_tup)
    timmy.circle(100)
    timmy.right(360/n_circles)

screen = Screen()
screen.exitonclick()

