import turtle as t

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

def draw_word(x,y,word):
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

draw_word("centered",0,"A B")
t.hideturtle()

t.done()