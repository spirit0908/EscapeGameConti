#-*-coding: utf-8-*-
from tkinter import *
import game1 as g
import game2 as g2
import game3 as g3

global game
f_game1 = 0
f_game2 = 0
f_game3 = 0
f_game4 = 0
remaining_time = 2400 #40min

class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def chrono(self, count=remaining_time):
        secondes = count
        minutes=int(count / 60)
        secondes %=60
        textTime.config(text="Time remaining: "+str(minutes)+"min "+str(secondes)+"s")
        if (count>0):
            self.after(1000,self.chrono,count-1)

    def initialize(self):
        self.grid()
        self.clear()
        #Game1:
        global buttonGame1
        buttonGame1 = Button(self,text="Unlock Desk", bg='cyan', width=10,height=5)
        buttonGame1.config(command=self.l_game1)
        buttonGame1.grid(row=1, column=1, columnspan=1)

        #can1 = Canvas(self)
        #can1.create_oval(5, 5, 20, 20, outline='red', fill='red', width=1)
        #can1.grid(row=2, column=3)
        
        #Game2:
        buttonGame2 = Button(self,text='Security Cam', bg='cyan', width=10,height=5,command=self.l_game2)
        buttonGame2.grid(row=1, column=3)

        #can2 = Canvas(self)
        #can2.create_oval(5, 5, 20, 20, outline='red', fill='red', width=1)
        #can2.grid(row=2, column=3)
        
        #Game3:
        buttonGame3 = Button(self,text='Game 3',width=10,height=5,command=self.l_game3)
        buttonGame3.grid(row=3, column=1)
        #textGame3 = Label(self, text="done", state="disabled").grid(row=4, column=1)

        #Game4:
        buttonGame4 = Button(self,text="Game 4",width=10,height=5,command=self.game4)
        buttonGame4.grid(row=3, column=3)
        #textGame4 = Label(self, text="done", state="disabled").grid(row=4, column=3)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(5,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(7,weight=1)
        #self.resizable(False,False)
        self.resizable(True,True)
        
        #Timer:
        start_s = remaining_time
        start_m = int(remaining_time / 60)
        start_s %= 60
        textTime = Label(self, text="Time remaining: "+str(start_m)+"min "+str(start_s)+"s",bg="white",width=25,relief="groove")
        textTime.grid(row=6, column=1, columnspan=4)
        self.chrono


    def clear(self):
        f = open("init.txt", "w")
        f.write('')
        f.close()
    

    def test_game(self, test):
        f = open("init.txt", "r")
        lines = f.readlines()
        for line in lines:
            if "finish_game1" or "finish_game2" in line:
                f.close()
                return 'true'
            else:
                f.close()
                return 'false'
        
    def l_game1(self):
        g.main()
        if self.test_game(1) == 'true':
            print("jeu 1 ok")
            f_game1 = 1
        return
         
    def l_game2(self):
        if self.test_game(1) == 'true':
            g2.main()
            if self.test_game(2) == 'true':
                print('jeu 2 Ok')
                game2 = 1
            else:
                print('no')
        else:
            messagebox.showinfo('Don\'t cheeat', "Unlock the desk first !")
        game2 = 0

    def l_game3(self):
        if self.test_game(2) == 'true':
            #g3.main()
            if self.test_game(3) == 'true':
                print('jeu 3 Ok')
                game3=1
            else:
                print('no')
        else:
            messagebox.showinfo('Don\'t cheeat', "Unlock the desk first !")
        game3 = 0

    def game4(self):
        if f_game3 == 1:
            game2=1
        else:
            messagebox.showinfo('Don\'t cheeat', "Recover your password first !")
        game4 = 0
    


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Escape Game Conti')
    app.geometry("250x390")
    app.mainloop()
