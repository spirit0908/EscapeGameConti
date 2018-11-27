#-*-coding: utf-8-*-
from tkinter import *
import time


remaining_time = 2401 #40min
debug = 'true'
pattern = 'badge'

class simplemaster_g4_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.sec = 0
        self.initialize()

    def ChangeCouleur(self,count):
        if count == 1:
            self.can1.config(bg='green')
        elif count == 2:
            self.can1.config(bg='green')
            self.can2.config(bg='green')
        elif count == 3:
            self.can1.config(bg='green')
            self.can2.config(bg='green')
            self.can3.config(bg='green')
        elif count == 4:
            self.can1.config(bg='green')
            self.can2.config(bg='green')
            self.can3.config(bg='green')
            self.can4.config(bg='green')
        else:
            return
        return
    
    def check_Badge(self):
        prev_badge = []
        ret = 'false'
        count = 0
        f = open("input_badge.txt", "r")
        lines = f.readlines()
        for line in lines:
            if pattern in line:
                if line not in prev_badge:
                    prev_badge.append(line)
                    count = count + 1
                    self.ChangeCouleur(count)
        f.close()
        if count > 3:
            ret = 'true'
        return ret

    def finish(self):
        self.lempty = Label(self, text="", state='disabled')
        self.lempty.grid(row=3, column=3, columnspan=3)
        self.label = Label(self, text="Well done !", bg='white', fg='red', width=25, relief='groove')
        self.label.grid(row=4, column=3, columnspan=3)
        f = open("init.txt", "a")
        f.write("finish_game4")
        f.close()

    
    def check_PreviousGames(self):
        ret = 'false'
        count = 0
        pat = str("finish_game")
        f = open("init.txt", "r")
        lines = f.readlines()
        for line in lines:
            if pat in line:
                count = count + 1
        f.close()
        if count == 2:
            ret = 'true'
        return ret
    
    def chrono(self):
        if self.check_PreviousGames() == 'true':
            if self.check_Badge() == 'true':
                self.finish()
            else:
                self.sec = self.sec + 1
                secondes = remaining_time - self.sec
                minutes= int((remaining_time - self.sec) / 60)
                secondes %= 60
                self.after(100,self.chrono)
        else:
            self.sec = self.sec + 1
            secondes = remaining_time - self.sec
            minutes= int((remaining_time - self.sec) / 60)
            secondes %= 60
            self.after(100,self.chrono)

    def clear(self):
        f = open("input_badge.txt", "w")
        f.write('')
        f.close()
        
    def initialize(self):
        self.grid()
        self.clear()
        
        self.can1 = Canvas(self, width=150, height=120, bg='red')
        txt1 = self.can1.create_text(75, 60, text='', fill='black')
        self.can1.grid(row=1, column=1)
            
        self.can2 = Canvas(self, width=150, height=120, bg='red')
        txt2 = self.can2.create_text(75, 60, text='', fill='black')
        self.can2.grid(row=1, column=3)

        self.can3 = Canvas(self, width=150, height=120, bg='red')
        txt3 = self.can3.create_text(75, 60, text='', fill='black')
        self.can3.grid(row=1, column=5)

        self.can4 = Canvas(self, width=150, height=120, bg='red')
        txt4 = self.can4.create_text(75, 60, text='', fill='black')
        self.can4.grid(row=1, column=7)
    
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(8,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.resizable(False,False)
        
        #Timer:
        self.chrono()


def main():
    master_g4 = simplemaster_g4_tk(None)
    master_g4.title('Open the god dame door !')
    master_g4.geometry("650x250")
    master_g4.mainloop()
