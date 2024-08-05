import turtle as t

def letters(letter):
  if letter == "A":
      t.goto(25,100)
      t.goto(50,0)
      t.up()
      t.goto(12,50)
      t.down()
      t.forward(25)

letters("A")

t.done()