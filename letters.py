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
    for i in word:
        draw_letter(x,y,100,200,i)

draw_word(-100,0,"AA")
t.hideturtle()

t.done()