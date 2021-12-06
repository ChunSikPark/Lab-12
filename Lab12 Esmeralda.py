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
  
# import messagebox from tkinter module
import tkinter.messagebox
  
# create a tkinter root window
root = tkinter.Tk()
  
# root window title and dimension
root.title("When you press a button the message will pop up")
root.geometry('500x300')
  
# Create a messagebox showinfo
  
def onClick():
    tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
  
# Create a Button
button = Button(root, text="Click Me", command=onClick, height=5, width=10)
  
# Set the position of button on the top of window.
button.pack(side='bottom')
root.mainloop()
