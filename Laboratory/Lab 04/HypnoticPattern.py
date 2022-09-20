#Hypnotic Pattern Algorithm
import turtle
turtle.hideturtle()
turtle.speed(0)

#NAMED CONSTANTS
START = 1
END = 999
STEP = 10

#START
for count in range (START,END,STEP):
    turtle.forward(count)
    turtle.setheading(turtle.heading()+90)
    print(count)
    
    
