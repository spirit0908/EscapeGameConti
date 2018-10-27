#-*-coding: utf-8-*-
from tkinter import *
import math

global game
game = 0

def game1():
    game = 1
     
def game2():
    game = 2

def game3():
    game = 3

def game4():
    game = 4


### Main ###

master = Tk()

master.title('Escape Game Conti') 
master.geometry()
#self.e = Entry(master)
#self.e.grid(row=0,column=0,columnspan=6,pady=3)
#self.e.focus_set() #Sets focus on the input text area

#Game1: 
Button(master,text="Game 1",width=10,height=8,command=lambda:game1()).grid(row=0, column=0,columnspan=1)
textGame1 = Label(master, text="done",height=5, width=5).grid(row=1, column=0)

#Game2:
Button(master,text='Game 2',width=10,height=8,command=lambda:game2()).grid(row=0, column=1)
textGame2 = Label(master, text="done").grid(row=1, column=1)

#Game3:
Button(master,text='Game 3',width=10,height=8,command=lambda:game3()).grid(row=2, column=0)
textGame3 = Label(master, text="done").grid(row=3, column=0)

#Game4:
Button(master,text="Game 4",width=10,height=8,command=lambda:game4()).grid(row=2, column=1)
textGame4 = Label(master, text="done").grid(row=3, column=1)

#Timer:
textTime = Label(master, text="Time remaining: 22 min").grid(row=4, column=0)


master.mainloop()

