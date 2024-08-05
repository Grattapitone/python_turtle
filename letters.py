import turtle as t
import math

t.shape("turtle")
t.fillcolor("blue")

def ellipse(a, b, h=None, k=None, angle=None, angle_unit=None):
    if h is None:
        h = 0
    if k is None:
        k = 0
    # Angle unit can be degree or radian
    if angle is None:
        angle = 360
        converted_angle = angle * 0.875
    if angle_unit == "d" or angle_unit is None:
        converted_angle = angle * 0.875
    # We are multiplying by 0.875 because for making a complete ellipse we are plotting 315 pts according
    # to our parametric angle value
    elif angle_unit == "r":
        converted_angle = (angle * 0.875 * (180/math.pi))
    # Converting radian to degrees.
    for i in range(int(converted_angle) + 1):
        if i == 0:
            t.up()
        else:
            t.down()
        t.setposition((h+a*math.sin(i/50)), (k + b * math.cos(i/50)))

def draw_letter(x,y,width,height,letter):
    t.up()
    t.goto(x,y)
    t.down()
    if letter == "A":
        t.goto(x + width / 2, y + height)
        t.goto(x + width,y)
        t.up()
        t.goto(x + width / 4, y + height / 2)
        t.down()
        t.forward(width / 2)
    elif letter == "B" or letter == "P":
        t.lt(90)
        t.forward(height)
        t.rt(90)
        ellipse(width,height / 4,x,y + height * (3/4),180)
        if letter == "B":
            ellipse(width,height / 4,x,y + height / 4,180)
    elif letter == " ":
        t.up()
        t.forward(width)
        t.down()
    else:
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)
        t.forward(width)
        t.lt(90)
        t.forward(height)
        t.lt(90)

def draw_word(word,y,x = "centered"):
    t.seth(0)
    if x == "centered":
        length = len(word) * 100 + (len(word) - 1) * 25
        xpos = length * -0.5
        for character in word:
            draw_letter(xpos,y,100,200,character)
            xpos += 125
    else:
        for character in word:
            draw_letter(x,y,100,200,character)
            x += 125

draw_word("ABP Z",0)
t.hideturtle()

t.done()