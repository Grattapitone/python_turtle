import turtle as t
import math

t.shape("turtle")
t.fillcolor("blue")

def ellipse(a, b, h=None, k=None, angle=None, negate1 = 1, negate2 = 1, orientation = "sincos", angle_unit=None):
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
        if orientation == "sincos":
            t.setposition(negate1*(h+a*math.sin(i/50)), negate2*(k + b * math.cos(i/50)))
        else:
            t.setposition(negate1*(h+a*math.cos(i/50)), negate2*(k + b * math.sin(i/50)))


def draw_letter(x,y,width,height,letter):
    t.seth(0)
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
    elif letter == "B" or letter == "P" or letter == "R":
        t.lt(90)
        t.forward(height)
        t.rt(90)
        ellipse(width,height / 4,x,y + height * (3/4),180)
        if letter == "B":
            ellipse(width,height / 4,x,y + height / 4,180)
        if letter == "R":
            t.goto(x + width,y)
    elif letter == "C":
        ellipse(width / 2, height / 2, -x - width / 2, y + height / 2,225,-1)
    elif letter == "D":
        t.lt(90)
        t.forward(height)
        t.rt(90)
        ellipse(width,height / 2,x,y + height / 2,180)
    elif letter == "E" or letter == "F":
        if letter == "E":
            t.forward(width)
            t.backward(width)
        t.lt(90)
        t.forward(height / 2)
        t.rt(90)
        t.forward(width)
        t.backward(width)
        t.lt(90)
        t.forward(height / 2)
        t.rt(90)
        t.forward(width)
    elif letter == "G":
        ellipse(width / 2, height / 2, -x - width / 2, y + height / 2,270,-1)
        t.backward(width / 2)
    elif letter == "H":
        t.lt(90)
        t.forward(height)
        t.backward(height / 2)
        t.rt(90)
        t.forward(width)
        t.rt(90)
        t.backward(height / 2)
        t.forward(height)
    elif letter == "I":
        t.forward(width)
        t.backward(width / 2)
        t.lt(90)
        t.forward(height)
        t.rt(90)
        t.backward(width / 2)
        t.forward(width)
    elif letter == "J":
        t.up()
        t.goto(x,y + height)
        t.down()
        t.forward(width)
        t.backward(width / 2)
        t.rt(90)
        t.forward(height * (3/4))
        ellipse(width / 4, height / 4, x + width / 4, -y - height / 4,180,1,-1,"cossin")
    elif letter == "K":
        t.lt(90)
        t.forward(height)
        t.backward(height / 2)
        t.rt(90)
        t.goto(x + width, y + height)
        t.setposition(x,y + height / 2)
        t.goto(x + width,y)
    elif letter == "L":
        t.goto(x, y + height)
        t.goto(x,y)
        t.forward(width)
    elif letter == "M":
        t.goto(x, y + height)
        t.goto(x + width / 2, y)
        t.goto(x + width, y + height)
        t.goto(x + width, y)
    elif letter == "N":
        t.goto(x, y + height)
        t.goto(x + width, y)
        t.goto(x + width, y + height)
    elif letter == "O" or letter == "Q":
        ellipse(width / 2, height / 2, x + width / 2, y + height / 2, )
        if letter == "Q":
            t.up()
            t.goto(x + width * (3/4), y + height / 4)
            t.down()
            t.goto(x + width,y)
    elif letter == "S":
        ellipse(width / 2, height / 4 - height / 16, x + width / 2, y + height * (3/4) + height / 16,270,1,1,"cossin")
        ellipse(width / 2, height / 4 + height / 16, x + width / 2, y + height / 4 + height / 16,270)
    elif letter == "T":
        t.up()
        t.forward(width / 2)
        t.down()
        t.lt(90)
        t.forward(height)
        t.rt(90)
        t.backward(width / 2)
        t.forward(width)
    elif letter == "U":
        t.up()
        t.goto(x, y + height)
        t.down()
        t.rt(90)
        t.forward(height * (3/4))
        ellipse(width / 2, height / 4, -x - width / 2, -y - height / 4, 180, -1, -1, "cossin")
        t.rt(180)
        t.forward(height * (3/4))
    elif letter == "V":
        t.up()
        t.goto(x, y + height)
        t.down()
        t.goto(x + width / 2, y)
        t.goto(x + width, y + height)
    elif letter == "W":
        t.up()
        t.goto(x, y + height)
        t.down()
        t.goto(x + width / 4, y)
        t.goto(x + width / 2, y + height)
        t.goto(x + width * (3/4), y)
        t.goto(x + width, y + height)
    elif letter == "X":
        t.goto(x + width, y + height)
        t.up()
        t.backward(width)
        t.down()
        t.goto(x + width, y)
    elif letter == "Y":
        t.up()
        t.goto(x, y + height)
        t.down()
        t.goto(x + width / 2, y + height / 2)
        t.rt(90)
        t.forward(height / 2)
        t.backward(height / 2)
        t.goto(x + width, y + height)
    elif letter == "Z":
        t.up()
        t.goto(x, y + height)
        t.down()
        t.forward(width)
        t.goto(x, y)
        t.forward(width)
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

def draw_word(width,height,word,y = "centered",x = "centered",Boldness = 10,spaceBetL = 25):
    t.width(Boldness)
    if x == "centered":
        length = len(word) * width + (len(word) - 1) * spaceBetL
        xpos = length * -0.5
        if y == "centered":
            ypos = -(height / 2)
            for character in word:
                draw_letter(xpos,ypos,width,height,character)
                xpos += width + spaceBetL
        else:
            for character in word:
                draw_letter(xpos,y,width,height,character)
                xpos += width + spaceBetL
    else:
        if y == "centered":
            for character in word:
                draw_letter(x,ypos,width,height,character)
                x += width + spaceBetL
        else:
            for character in word:
                draw_letter(x,y,width,height,character)
                x += width + spaceBetL
t.speed("fastest")
"""draw_word(100,200,"ATTENTION",200,Boldness = 30,spaceBetL = 30)
draw_word(50,100,"READING THIS SIGN",0)
draw_word(50,100,"COULD CAUSE",-125)
draw_word(50,100,"SERIOUS ACCIDENTS",-250)"""
draw_word(100,200,"XYZç")
t.hideturtle()

t.done()