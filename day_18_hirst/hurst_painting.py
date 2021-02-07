import colorgram as cg
import canvasvg
import turtle
import random as rnd

turtle.colormode(255)

extracted_colors = cg.extract("real_hirst.jpeg", 30)
rgb_colors = []
for color in extracted_colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    rgb_colors.append((r,g,b))

print(rgb_colors)
print(rnd.choice(rgb_colors))


timmy = turtle.Turtle()
timmy.hideturtle()
screen = turtle.Screen()
timmy.speed(0)
timmy.penup()
timmy.pensize(20)
for xx in range(-325, 1975, 65):
    for yy in range(-325, 975, 65):
        timmy.goto(xx,yy)
        timmy.color(rnd.choice(rgb_colors))
        timmy.pendown()
        timmy.circle(10)
        timmy.penup()


#screen = turtle.Screen()
#screen.exitonclick()

ts = turtle.getscreen().getcanvas()
canvasvg.saveall("my_hirst.svg", ts)