# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 11:30:29 2021

@author: brian
"""

    # By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    #
    # Names:        Brian Lee
    #               Kylie Thomas
    #              Esmeralda Garcia
    #               Jennifer Cortez
    # Section:      514
    # Assignment:   Lab 12
    # Date:         06 12 2021
    # 
    
import turtle as t

t.speed(900)
t.pensize(8)
t.penup()
t.goto(0,-150)
t.pendown()

#head
t.pencolor("pink")
t.fillcolor("pink")
t.begin_fill()
for i in range(36):
    t.forward(30)
    t.left(10)
t.end_fill()

#eye1
t.pencolor("black")
t.penup()
t.goto(-80,0)
t.pendown()
t.fillcolor("black")
t.begin_fill()
'''
for i in range(180):
    t.forward(1)
    t.left(2)
'''
t.circle(30)
t.end_fill()

#eye2
t.penup()
t.goto(110,0)
t.pendown()
t.begin_fill()
'''
for i in range(180):
    t.forward(1)
    t.left(2)
'''
t.circle(30)
t.end_fill()

#snoot
t.pencolor('#c9759b')
t.penup()
t.goto(-30,-50)
t.pendown()
t.fillcolor('#c9759b')
t.begin_fill()
t.seth(-45)
for i in range(2):
    t.circle(60,90)
    t.circle(60//2,90)
t.end_fill()

#nostril1
t.pencolor("#994b6e")
t.penup()
t.goto(-30,-40)
t.pendown()
t.fillcolor("#994b6e")
t.begin_fill()
for i in range(15):
    t.circle(20,40)
t.end_fill()

#nostril2
t.pencolor("#994b6e")
t.penup()
t.goto(35,-7)
t.pendown()
t.fillcolor("#994b6e")
t.begin_fill()
for i in range(15):
    t.circle(20,40)
t.end_fill()

#ear1
t.penup()
t.pencolor("pink")
t.goto(-140,90)
t.fillcolor("pink")
t.begin_fill()
t.pendown()
t.left(65)
t.forward(75)
t.right(125)
t.forward(130)
t.right(145)
t.forward(107)
t.end_fill()

#ear2
t.penup()
t.pencolor("pink")
t.goto(170,90)
t.fillcolor("pink")
t.begin_fill()
t.pendown()
t.left(155)
t.forward(75)
t.left(135)
t.forward(130)
t.left(145)
t.forward(93)
t.end_fill()

t.mainloop()
