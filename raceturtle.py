from turtle import Turtle, Screen
import random


d =["red", "yellow", "orange", "blue", "purple", "green"]
new =[]
ypos = [-70, -40, -10, 20, 50, 80]
s = Screen()
s.setup(width=500, height=400)

ubet = s.textinput(title="make your bet ", prompt="which turtle will win the race? enter the color?")
if ubet == None:
    sys.exit(0)



game = False
for i in range(0, 6):
    nwturtle = Turtle(shape="turtle")
    nwturtle.penup()
    nwturtle.color(d[i])
    nwturtle.goto(x=-230, y=ypos[i])
    new.append(nwturtle)

if ubet:
    game = True
wining = None
while game:
    for i in new:
        d = random.randint(0,10)
        i.forward(d)
    if i.xcor() > 230:
        wining = i.pencolor()
        game = False
        if ubet == wining:
            print(f"you win {wining}")
        elif ubet != wining:
            print(f"you lose winner is {wining}")

s.exitonclick()

