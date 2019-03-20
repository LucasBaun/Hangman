#!/bin/python3

from turtle import*
from random import randint

speed(15)
penup()
goto(-140, 140)

for step in range(16):
  write(step, align='center')
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)

ada = Turtle()
ada.color('red')
ada.shape('arrow')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

eve = Turtle()
eve.color('green')
eve.shape('classic')

eve.penup()
eve.goto(-160,40)
eve.pendown()

uwu = Turtle()
uwu.color('yellow')
uwu.shape('circle')

uwu.penup()
uwu.goto(-160,10)
uwu.pendown()

speed(2)

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  eve.forward(randint(1,5))
  uwu.forward(randint(1,5))
