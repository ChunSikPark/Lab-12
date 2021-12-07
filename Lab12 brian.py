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
import random

#Main menu window
window = Tk()
window.title("Welcome to the Pig Game!!")
window.geometry("700x700")
window.configure(background='#d0ae9b') #Set the background color

label1 = Label(window,text='',font=('Helvetica',15))

def main ():
    "This Function shows the rule of the game that player has to follow"
    label= Label(text='Welcome to the pig game! \n1. The game involves two players. \n2. A player repeatedly rolls a dice until they decide to hold or roll a one. \n3. If a player decides to hold then player keep the point and end his turn \n4. If they roll a one then they are automatically out of the game and the other player wins. \n5. If the player rolls any number other than one then it is added to their total. \n6. Then the player continues to roll the dice. \n7. The player who has more points is the winner') #Fix label1 as Player 1
    label.pack()
    
    label1 = Label(text="Do not press roll button once you get BUSTED!",font=('Helvetica',25))
    label1.configure(background='#d0ae9b')
    label1.pack()




def button_play():
    "This function is when player press the play button, it closes the main menu window and take player"
    "to the game window"
    window.destroy()

#Two buttons on main menu
button1 = Button(window,text = "Rules", command = main,padx=10,pady=10,fg = "black") #For Rule
button1.pack()
button = Button(text = "Play", command = button_play,padx=10,pady=10,fg = "red") #For play
button.pack()


window.mainloop()

#Player 1's Turn
root = Tk()

root.title("Player 1's Turn") #Title of the window
root.geometry("600x600") #Size of the window
root.configure(background='#d0ae9b') #Set the background color to specific color
label1 = Label(root,text='', font=('Helvetica',30))
label = Label(root, text='',font=('Helvetica',150))
label2 = Label(root,text='',font=('Helvetica',30))
count = 0



def roll_dice():
    "This function roll the dice for player 1. It will roll the dice randomly. If user gets 1 from the dice"
    "Then player 1 considered as busted from the game. In other words, player 1 losese the game. Otherwise, "
    "Player 1 gets the point as much as the number of the dice's number"
    
    label1.configure(text='Player 1',background='#d0ae9b') #Fix label1 as Player 1
    label1.pack()
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] #Using Unicode character, we can show dice to user
    d = {'\u2680':1,'\u2681':2,'\u2682':3,'\u2683':4,'\u2684':5,'\u2685':6} #Number of dice
    dice_roll = random.choice(dice) #Randomly roll the dice
    global count
    if d[dice_roll]== 1: #when player 1 gets 1 from dice, he busted
        label.configure(text='Bust!',font=("helvetica",150),background='#d0ae9b')
        label.pack()
        count = 0 #his point become 0

        label3 = Label(root, text="You Got Busted!",font=("helvetica",30)) #If user busted, print you got busted
        label3.configure(background='#d0ae9b')
        label3.pack()
        root.after(1500,lambda: root.destroy()) #If user busted, close window 2 seconds later
    else:
        label.configure(text=f'{dice_roll}',background='#d0ae9b') #Other wise, shows the face of dice and add points
        label.pack()
        count+= int(d[dice_roll])
    label2.configure(text= count,background='#d0ae9b') #Print total points of plyaer 1
    label2.pack()

button = Button(root,text='Roll dice', command = roll_dice,padx=10,pady=10) #Button to roll the dice
button.pack()

button2 = Button(root,text='Hold',command = root.destroy, padx=10,pady=10) #Button to hold
button2.pack()
root.mainloop()



# =============================================================================
# #Code for player 2 is exaclty same as player1, So I will skip commenting    #
# =============================================================================

#Player 2's Turn
root = Tk()

root.title("Plyaer 2's Turn")
root.geometry("600x600")
root.configure(background='#d0ae9b')
label1 = Label(root,text='', font=('Helvetica',30))
label = Label(root, text='',font=('Helvetica',150))
label2 = Label(root,text='',font=('Helvetica',30))
count2 = 0
def roll_dice_2():
    "This function works exactly same as the function for player 1."
    label1.configure(text='Player 2',background='#d0ae9b')
    label1.pack()
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    d = {'\u2680':1,'\u2681':2,'\u2682':3,'\u2683':4,'\u2684':5,'\u2685':6}
    dice_roll = random.choice(dice)
    global count2
    if d[dice_roll]== 1:
        label.configure(text='Bust!',font=("helvetica",150),background='#d0ae9b')
        label.pack()
        count2 = 0
        label3 = Label(root, text="You Got Busted!",font=("helvetica",30)) 
        label3.configure(background='#d0ae9b')
        label3.pack()
        root.after(1500,lambda: root.destroy())
    else:
        label.configure(text=f'{dice_roll}',background='#d0ae9b')
        label.pack()
        count2 += int(d[dice_roll])
    label2.configure(text= count2,background='#d0ae9b')
    label2.pack()

#Button for player2, works exactly same as player 1's button
button4 = Button(root,text='Roll dice', command = roll_dice_2,padx=10,pady=10)
button4.pack()

button5 = Button(root,text='Hold',command = root.destroy, padx=10,pady=10)
button5.pack()

root.mainloop()

#Pop up screen to show the result of the game
root = Tk()

root.title("Result")
root.geometry("600x600")
root.configure(background='#d0ae9b')
label1 = Label(root, text="Player1's Score: "+ f'{count}',font=('Helvetica',30)) #Print Player 1's score
label1.configure(background='#d0ae9b')
label1.pack()
label2 = Label(root, text="Player2's Score: "+ f'{count2}',font=('Helvetica',30)) #Print Player 2's score
label2.configure(background='#d0ae9b')
label2.pack()
label = Label(root,text='',font=('Helvetica',30))
if count2 > count:
    label.configure(text="Player2 Wins!",background='#d0ae9b') #Modity label to player 2 wins if player 2 have more points
    label.pack()
elif count > count2:
    label.configure(text="Player1 Wins!",background='#d0ae9b') #Modity label to player 1 wins if player 2 have more points
    label.pack()
elif count == count2:
    label.configure(text="Draw",background='#d0ae9b') #Modity label to player 1 wins if player 2 have more points
    label.pack()


root.mainloop()


    
