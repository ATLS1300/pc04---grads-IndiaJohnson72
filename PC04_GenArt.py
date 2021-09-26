"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: India Johnson

********* HEY, READ THIS FIRST **********

Generative Art processing piece that  includes two different spiral designs and one chuncky square.
These designs are using the random key function that allow is to choice a random location and color palette.


"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

panel = turtle.Screen()
w = 600 
h = 600 
panel.setup(w, h)  

panel.bgcolor("gold2") #panel color

grayPalette = ["darkslategray1", "darkslategray2", "darkslategray3"]
honeydewPalette = ["honeydew", "honeydew1", "honeydew2"]

palette = random.choice([grayPalette, honeydewPalette])

spiral = turtle.Turtle()

circle = turtle.Turtle()

largeSquare= turtle.Turtle()

smallSquare=turtle.Turtle()

largeSpiral = turtle.Turtle()


a = turtle.Turtle()

#=============================
#spiral with circles and random palette  selction

spiral.speed(100)
spiral.width(10)


for i in range(30):
    spiral.up() #pick up pen
    spiral.color(random.choice(palette))
    spiral.forward(i)
    spiral.right(20)
    
    spiral.down()
    spiral.circle(4)
    spiral.left(90)
    spiral.backward(2)
    spiral.right(90)
    
#===================================
#largeSpiral design with random (x,y) $ palette

largeSpiral.up()
largeSpiral.speed(200)

largeSpiral.goto(random.randint(100,200),random.randint(100,200)) 
    
for i in range(50):
    largeSpiral.down() #pick up pen
    largeSpiral.color(random.choice(palette))
    largeSpiral.forward(i)
    largeSpiral.right(20)
    largeSpiral.down()
    largeSpiral.left(90)
    largeSpiral.backward(2)
    largeSpiral.right(90)
    
#==================================
#small open square design with random color palette

smallSquare.up()
smallSquare.speed(100)
smallSquare.width(40)

smallSquare.goto(random.randint(-100,200),random.randint(-100,200))

#============ borrowed from Tyler Dupuy

for i in range(8):
    smallSquare.down()
    smallSquare.color(random.choice(palette))
    smallSquare.forward(50)
    smallSquare.left(90)
    
turtle.done()

