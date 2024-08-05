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

draw_letter(-250,0,500,30,"A")
t.hideturtle()

t.done()