# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:59:29 2021

@author: brian
"""
from tkinter import *
import random
root = Tk()

root.title("Player 1's Turn")
root.geometry("600x600")

label1 = Label(root,text='', font=('Helvetica',30))
label = Label(root, text='',font=('Helvetica',150))
label2 = Label(root,text='',font=('Helvetica',30))
count = 0


def roll_dice():
    label1.configure(text='Player 1')
    label1.pack()
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    d = {'\u2680':1,'\u2681':2,'\u2682':3,'\u2683':4,'\u2684':5,'\u2685':6}
    dice_roll = random.choice(dice)
    global count
    if d[dice_roll]== 1:
        label.configure(text='Bust!',font=("helvetica",150))
        label.pack()
        count = 0
    else:
        label.configure(text=f'{dice_roll}')
        label.pack()
        count+= int(d[dice_roll])
    label2.configure(text= count)
    label2.pack()

button = Button(root,text='Roll dice', command = roll_dice,padx=10,pady=10)
button.pack()

button2 = Button(root,text='Hold',command = root.destroy, padx=10,pady=10)
button2.pack()

button3 = Button(root,text='I Got Busted',command = root.destroy,padx=10,pady=10)
button3.pack()
root.mainloop()

root = Tk()

root.title("Plyaer 2's Turn")
root.geometry("600x600")
label1 = Label(root,text='', font=('Helvetica',30))
label = Label(root, text='',font=('Helvetica',150))
label2 = Label(root,text='',font=('Helvetica',30))
count2 = 0
def roll_dice_2():
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
  
button4 = Button(root,text='Roll dice', command = roll_dice_2,padx=10,pady=10)
button4.pack()

button5 = Button(root,text='Hold',command = root.destroy, padx=10,pady=10)
button5.pack()

button6 = Button(root,text='I Got Busted',command = root.destroy,padx=10,pady=10)
button6.pack()

root.mainloop()



root = Tk()

root.title("Result")
root.geometry("600x600")

label1 = Label(root, text="Player1's Score: "+ f'{count}',font=('Helvetica',30))
label1.pack()
label2 = Label(root, text="Player2's Score: "+ f'{count2}',font=('Helvetica',30))
label2.pack()
label = Label(root,text='',font=('Helvetica',30))
if count2 > count:
    label.configure(text="Player2 Wins!")
    label.pack()
else:
    label.configure(text="Player1 Wins!")
    label.pack()

root.mainloop()






