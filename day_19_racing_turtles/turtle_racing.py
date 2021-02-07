from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("grey")

# Game properties and set-up
initial_x_position = -200
finish_line_x = 350
max_step_size = 10
distance_travelled = [0, 0, 0, 0, 0, 0]
y_positions = [150, 90, 30, -30, -90, -150]
colours = ["red", "orange", "yellow", "green", "blue", "violet"]
tims = []

# Initialise turtles
for i in range(0, len(colours)): # i is turtle index
    tims.append(Turtle(shape ="turtle"))
    tims[i].color(colours[i])
    tims[i].penup()
    tims[i].goto(initial_x_position, y_positions[i])

# Ask user for their guess
user_bet = screen.textinput(
    title="Place your bets!",
    prompt="Which turtle do you think will win the race? Enter a colour: \n\t (Red, Yellow, Green, Blue, Violet)")
user_bet = user_bet.lower()
print(f"You placed your bet on {user_bet}. \n 🏁 Off they go!")

# Run the race
no_winner_yet = True

while no_winner_yet:
    for turtle_index in range(0, len(tims)):                        # sequentially progress turtles and check for winner
        if no_winner_yet:
            step_size = random.randint(0, max_step_size)
            tims[turtle_index].forward(step_size)
            distance_travelled[turtle_index] += step_size
            no_winner_yet = max(distance_travelled) < finish_line_x
            winning_colour = colours[turtle_index]

# Report the result
if winning_colour == user_bet:
    print(f"🏁 The {winning_colour} turtle won the race. Congratulation, you won your bet! 🥳 ")
else:
    print(f"🏁The {winning_colour} turtle won the race. You lost your bet 😞")




screen.exitonclick()
