#-*-coding: utf-8-*-
from tkinter import *
import game1 as g
import game2 as g2
import game3 as g3
import game4 as g4
import time
import unicodedata

global game
f_game1 = 0
f_game2 = 0
f_game3 = 0
f_game4 = 0
remaining_time = 2401 #40min
debug = 'true'
pwd = 'SoftwarePlatform'

class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.sec = 0
        self.initialize_bis()

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii

    def finish(self):
        self.lfinsih = Label(self, text="Well done !", state="normal",fg='red', bg='white',relief="groove",width=25).grid(row=8, column=1, columnspan=4)
        self.bfinish = Button(self, text="Quit", command=self.destroy)
        self.bfinish.grid(row=6, column=3)
        
    def loose(self):
        self.lloose = Label(self, text='You lost !', state="normal",fg='red', bg='white',relief="groove",width=35).grid(row=7, column=1, columnspan=4)
        self.lfinsih = Label(self, text="You are now part of Christmas elves !", state="normal",fg='red', bg='white',relief="groove",width=35).grid(row=8, column=1, columnspan=4)
        self.buttonGame4.config(state='disabled')
        self.buttonGame3.config(state='disabled')
        self.buttonGame2.config(state='disabled')
        self.buttonGame1.config(state='disabled')
        self.bfinish = Button(self, text="Quit", command=self.destroy)
        self.bfinish.grid(row=6, column=3)

    def chrono(self):
        if (self.test_game(4) == 'true'):
            self.buttonGame4.config(bg='green',text='Game 4\nUnlocked')
            self.finish()
        elif (self.sec == remaining_time):
            self.loose()
        else:
            self.sec = self.sec + 1
            secondes = remaining_time - self.sec
            minutes= int((remaining_time - self.sec) / 60)
            secondes %= 60
            self.textTime.config(text="Time remaining: "+str(minutes)+"min "+str(secondes)+"s")
        if (self.sec > 0):
            self.after(1000,self.chrono)

    def login(self):
        user_answer = self.remove_accents(self.entry_login.get())
        s_pwd = self.remove_accents(pwd)
        if user_answer.lower() == s_pwd.lower():
            self.initialize()
        return
    
    def reset_doc(self):
        f = open("input_badge.txt", "w")
        f.write('')
        f.close()
        f = open("init.txt", "w")
        f.write('')
        f.close()
        
    def initialize_bis(self):
        self.reset_doc()
        
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)
        self.lempty = Label(self, text="", padx=200, pady=200).grid(row=0, column=0, sticky='nsew')
        self.lempty2 = Label(self, text="", padx=200, pady=200).grid(row=0, column=10, sticky='nsew')
        self.lempty3 = Label(self, text="", padx=200, pady=200).grid(row=10, column=0, sticky='nsew')
        self.lempty4 = Label(self, text="", padx=200, pady=200).grid(row=10, column=10, sticky='nsew')
        
        self.lbl = Label(self, text="User:", relief='groove', padx=25)
        self.lbl.grid(row=1, column=1, columnspan=2)
        
        self.entry_login = Entry(self, width=50, show='*')
        self.entry_login.grid(row=1, column=2, columnspan=3)
        
        self.btn_Ok = Button(self, text="Ok", command=self.login)
        self.btn_Ok.grid(row=2, column=1, columnspan=2)
        
        self.btn_Cancel = Button(self, text="Cancel", state='disabled')
        self.btn_Cancel.grid(row=2, column=2, columnspan=2)
        
        self.btn_Forget = Button(self, text="Password Forgotten ?", command=self.l_game1)
        self.btn_Forget.grid(row=2, column=3, columnspan=2)
        
        if debug == 'true':
            button = Button(self, text="Debug_Quit", command=self.destroy)
            button.grid(row=4, column=3)

        #Timer:
        start_s = remaining_time
        start_m = int(remaining_time / 60)
        start_s %= 60
        self.textTime = Label(self, text="Time remaining: "+str(start_m)+"min "+str(start_s)+"s",bg="white",width=25,relief="groove")
        self.textTime.grid(row=6, column=1, columnspan=4)
        self.chrono()

    def UnlcokDesk(self):
        self.buttonGame1.config(text="Desk\nUnlocked", bg='green')
        
    def initialize(self):
        #self.grid()
        self.clear()
        
        #Game1:
        global buttonGame1
        self.buttonGame1 = Button(self,text="Desk\nLocked", bg='red', width=15,height=5, command=self.UnlcokDesk)
        self.buttonGame1.grid(row=1, column=1, columnspan=1)
        textGame1 = Label(self, text="", state="disabled").grid(row=2, column=1)

        #Game2:
        self.buttonGame2 = Button(self,text='For motivations', bg='grey', width=15,height=5,command=self.l_game2)
        self.buttonGame2.grid(row=1, column=3)
  
        #Game3:
        self.buttonGame3 = Button(self,text='Security Camera', bg='red', width=15,height=5,command=self.l_game3)
        self.buttonGame3.grid(row=3, column=1)
        textGame3 = Label(self, text="", state="disabled").grid(row=2, column=2)

        #Game4:
        self.buttonGame4 = Button(self,text="Game 4\nLocked",bg='red', width=15,height=5,command=self.l_game4)
        self.buttonGame4.grid(row=3, column=3)
        textGame4 = Label(self, text="", state="disabled").grid(row=4, column=2)

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(7,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.resizable(False,False)
        
        #Timer:
        start_s = remaining_time
        start_m = int(remaining_time / 60)
        start_s %= 60
        self.textTime = Label(self, text="Time remaining: "+str(start_m)+"min "+str(start_s)+"s",bg="white",width=25,relief="groove")
        self.textTime.grid(row=6, column=1, columnspan=4)
        self.chrono()

    def clear(self):      
        self.lbl.destroy()
        self.entry_login.destroy()
        self.btn_Ok.destroy()
        self.btn_Cancel.destroy()
        self.btn_Forget.destroy()

    def test_game(self, test):
        ret = 'false'
        f = open("init.txt", "r")
        pattern = str("finish_game"+str(test))
        lines = f.readlines()
        for line in lines:
            if pattern in line:
                ret = 'true'
        f.close()
        return ret
    
    def l_game1(self):
        g.main()
        if self.test_game(1) == 'true':
            if debug=='true':print("jeu 1 ok")
            f_game1 = 1
         
    def l_game2(self):
        top = Toplevel()

        can1 = Canvas(top, width = 550, height = 428, bg = 'white')
        p = PhotoImage(file='papanowel.gif')
        item = can1.create_image(250, 228, image=p)
        can1.image = p
        can1.grid()

    def l_game3(self):
        top = Toplevel()

        btn1 = Button(top, text='Ok', command=self.security_cam)
        btn1.grid(row=2, column=2)

        self.ent1 = Entry(top, width=2, bg='white')
        self.ent1.grid(row=1, column=1)
        
        self.ent2 = Entry(top, width=2, bg='white')
        self.ent2.grid(row=1, column=2)
        
        self.ent3 = Entry(top, width=2, bg='white')
        self.ent3.grid(row=1, column=3)
        
        self.ent4 = Entry(top, width=2, bg='white')
        self.ent4.grid(row=1, column=4)

        self.bindic = Button(top, bitmap='question',command=lambda:messagebox.showinfo('Indice','Are you \'phone connected\' ?'))
        self.bindic.grid(row=2, column=4)
        
    def security_cam(self):
        if (self.ent1.get() == str(1)) and (self.ent2.get() == str(8)) and (self.ent3.get() == str(5)) and (self.ent4.get() == str(5)):
            messagebox.showinfo('','video link')
            #TODO ajouter lien vidéo
        return
    
    def l_game4(self):
        g4.main()


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Escape Game Conti')
    app.attributes('-fullscreen', 1)
    #app.geometry("250x350")
    app.mainloop()
