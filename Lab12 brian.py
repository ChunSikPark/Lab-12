# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:59:29 2021

@author: brian
"""
from tkinter import *
import random


#Player 1's Turn
root = Tk()

root.title("Player 1's Turn")
root.geometry("600x600")

label1 = Label(root,text='', font=('Helvetica',30))
label = Label(root, text='',font=('Helvetica',150))
label2 = Label(root,text='',font=('Helvetica',30))
count = 0


def roll_dice():
    "This function roll the dice for player 1. It will roll the dice randomly. If user gets 1 from the dice"
    "Then player 1 considered as busted from the game. In other words, player 1 losese the game. Otherwise, "
    "Player 1 gets the point as much as the number of the dice's number"
    
    label1.configure(text='Player 1') #Fix label1 as Player 1
    label1.pack()
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] #Using Unicode character, we can show dice to user
    d = {'\u2680':1,'\u2681':2,'\u2682':3,'\u2683':4,'\u2684':5,'\u2685':6} #Number of dice
    dice_roll = random.choice(dice) #Randomly roll the dice
    global count
    if d[dice_roll]== 1: #when player 1 gets 1 from dice, he busted
        label.configure(text='Bust!',font=("helvetica",150))
        label.pack()
        count = 0 #his point become 0
    else:
        label.configure(text=f'{dice_roll}') #Other wise, shows the face of dice and add points
        label.pack()
        count+= int(d[dice_roll])
    label2.configure(text= count) #Print total points of plyaer 1
    label2.pack()

button = Button(root,text='Roll dice', command = roll_dice,padx=10,pady=10) #Button to roll the dice
button.pack()

button2 = Button(root,text='Hold',command = root.destroy, padx=10,pady=10) #Button to hold
button2.pack()

button3 = Button(root,text='I Got Busted',command = root.destroy,padx=10,pady=10) #If user busted, has to press this button
button3.pack()
root.mainloop()


#Player 2's Turn
root = Tk()

root.title("Plyaer 2's Turn")
root.geometry("600x600")
label1 = Label(root,text='', font=('Helvetica',30))
label = Label(root, text='',font=('Helvetica',150))
label2 = Label(root,text='',font=('Helvetica',30))
count2 = 0
def roll_dice_2():
    "This function works exactly same as the function for player 1."
    label1.configure(text='Player 2')
    label1.pack()
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    d = {'\u2680':1,'\u2681':2,'\u2682':3,'\u2683':4,'\u2684':5,'\u2685':6}
    dice_roll = random.choice(dice)
    global count2
    if d[dice_roll]== 1:
        label.configure(text='Bust!',font=("helvetica",150))
        label.pack()
        count2 = 0
    else:
        label.configure(text=f'{dice_roll}')
        label.pack()
        count2 += int(d[dice_roll])
    label2.configure(text= count2)
    label2.pack()

#Button for player2, works exactly same as player 1's button
button4 = Button(root,text='Roll dice', command = roll_dice_2,padx=10,pady=10)
button4.pack()

button5 = Button(root,text='Hold',command = root.destroy, padx=10,pady=10)
button5.pack()

button6 = Button(root,text='I Got Busted',command = root.destroy,padx=10,pady=10)
button6.pack()

root.mainloop()



#Pop up screen to show the result of the game
root = Tk()

root.title("Result")
root.geometry("600x600")

label1 = Label(root, text="Player1's Score: "+ f'{count}',font=('Helvetica',30)) #Print Player 1's score
label1.pack()
label2 = Label(root, text="Player2's Score: "+ f'{count2}',font=('Helvetica',30)) #Print Player 2's score
label2.pack()
label = Label(root,text='',font=('Helvetica',30))
if count2 > count:
    label.configure(text="Player2 Wins!") #Modity label to player 2 wins if player 2 have more points
    label.pack()
else:
    label.configure(text="Player1 Wins!") #Modity label to player 1 wins if player 2 have more points
    label.pack()

root.mainloop()






