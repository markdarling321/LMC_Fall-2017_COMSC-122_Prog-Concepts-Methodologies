#Mark Darling - COMSC 122-0940 - Lab 03B
#53 degrees angle is the perfect bearing
#8.3 misses the target
#8.4 hits the target
#8.5 force hits the target
#8.6 misses the target
#8.7 misses the target
#8.8 misses the target


#Hit the Target Game
import turtle

#Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 150
TARGET_LLEFT_Y = 200
TARGET_WIDTH = 5
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

#Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

#Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

#Center the turtle.
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

#Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

#Calculate the distance.
distance = force * FORCE_FACTOR

#Set the heading.
turtle.setheading(angle)

#Launch the projectile.
turtle.pendown()
turtle.forward(distance)

#Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_Y + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')
else:
        print('You missed the target.')
