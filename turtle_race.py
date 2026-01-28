from turtle import Turtle, Screen
import random

# Setup screen
screen = Screen()
screen.setup(width=500, height=400)

# Ask user to place bet
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color:"
)

# Colors and positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

# Create turtles
for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(turtle)

race_on = False

if user_bet:
    race_on = True

# Start race
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet.lower():
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()