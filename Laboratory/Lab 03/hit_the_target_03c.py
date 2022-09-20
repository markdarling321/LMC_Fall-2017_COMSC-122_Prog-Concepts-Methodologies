#Mark Darling - COMSC 122-0940 - Lab 03C
#56 degrees angle is the perfect bearing
#9.20 hits pretty darn close to the center


#Hit the Target Game
import turtle

#Named constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 150
TARGET_LLEFT_Y = 200
TARGET_RADIUS = 25
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
turtle.circle(TARGET_RADIUS)
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
if (turtle.distance(TARGET_LLEFT_X, TARGET_LLEFT_Y + TARGET_RADIUS) <= TARGET_RADIUS):
        print('Target hit!')
else:
        print('You missed the target.')
