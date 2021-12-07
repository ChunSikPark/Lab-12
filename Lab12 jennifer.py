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
from tkinter import *


window = Tk()
window.title("Welcome to the Pig Game!!")
window.geometry("700x700")
window.configure(background='#d0ae9b')

label1 = Label(window,text='',font=('Helvetica',15))

def main ():
    label= Label(text='Welcome to the pig game! \nThe game involves two players. \nA player repeatedly rolls a dice until they decide to hold or roll a one. \nIf a player decides to hold then their score does not change \nand\nIf they roll a one then they are automatically out of the game and the other player wins. \nIf the player rolls any number other than one then it is added to their total. \nThen the player continues to roll the dice.') #Fix label1 as Player 1
    label.pack()
button1 = Button(window,text = "Rules", command = main,padx=10,pady=10,fg = "black")
button1.pack()

def button_exit():
    window.destroy()

button = Button(text = "Exit", command = button_exit,padx=10,pady=10,fg = "red")
button.pack()


window.mainloop()

    
    
