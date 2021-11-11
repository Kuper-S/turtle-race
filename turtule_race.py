from turtle import Turtle,Screen

import random

colors = ["red","orange","yellow","green","blue","purple"]


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bets = screen.textinput(title="Make your bet",prompt="Wich turtle will win the race? Enter a color: ")
y_position = [90,60,30,0,-30,-60]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bets:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bets:
                print(f"Your bet was correct! The {winner} turtle won the rcae! ")
            else:
                print(f"Sorry your "
                      f"turtle lost the race to the {winner} turtle...")



screen.exitonclick()