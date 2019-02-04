""" Just take some break by drawing shapes. You can explore to end up with cooler ones than these."""

import turtle 
from turtle import *

def draw_square(some):   
    num_steps = 4
    begin_step = 0
    
    while (begin_step < num_steps):
        some.forward(150)
        some.right(90)
  
def draw_art():
    window = turtle.Screen()
    window.bgcolor('green')
    
    me = turtle.Turtle()
    for i in range(1, 37):
        draw_square(me)
        me.right(10)
        
    window.exitonclick()
   
def draw_star():
    speed(2)
    begin_fill()
    while True:
        forward(200)
        right(120)
        right(5)
        
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    
    window.exitonclick()
    
 
    
# draw_square(some)
# draw_art()
draw_star()