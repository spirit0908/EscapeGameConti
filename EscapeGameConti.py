#-*-coding: utf-8-*-
from tkinter import *
import game1 as g1
import game4 as g4
import time
import unicodedata
import subprocess

remaining_time = 2401 #40min
debug = 'true'
pwd = 'SoftwarePlatform'

class simpleapp_tk(Tk):
    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        self.sec = 0
        self.pre_initialize()

    def remove_accents(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        only_ascii = nfkd_form.encode('ASCII', 'ignore')
        return only_ascii

    def finish(self):
        self.lfinsih = Label(self, text="Well done !", state="normal",fg='red', bg='white',relief="groove",width=25,font=self.font).grid(row=8, column=1, columnspan=4)
        self.bfinish = Button(self, text="Quit", command=self.destroy, font=self.font)
        self.bfinish.grid(row=10, column=3)
        subprocess.call("./unlock.sh",shell=True)
        subprocess.call("./music.sh",shell=True)
        
    def loose(self):
        self.lloose = Label(self, text='You lost !', state="normal",fg='red', bg='white',relief="groove",width=35,font=self.font).grid(row=7, column=1, columnspan=4)
        self.lfinsih = Label(self, text="You are now part of Christmas elves !", state="normal",fg='red', bg='white',relief="groove",width=35,font=self.font).grid(row=8, column=1, columnspan=4)
        self.buttonGame4.config(state='disabled')
        self.buttonGame3.config(state='disabled')
        self.buttonGame2.config(state='disabled')
        self.buttonGame1.config(state='disabled')
        self.bfinish = Button(self, text="Quit", command=self.destroy,font=self.font)
        self.bfinish.grid(row=10, column=3)

    def chrono(self):
        if (self.test_game(4) == 'true'):
            self.buttonGame4.config(bg='green',text='Lockdown \nDisengaged',font=self.font)
            self.finish()
        elif (self.sec == remaining_time):
            self.loose()
        else:
            self.sec = self.sec + 1
            secondes = remaining_time - self.sec
            minutes= int((remaining_time - self.sec) / 60)
            secondes %= 60
            self.textTime.config(text="Time remaining: "+str(minutes)+"min "+str(secondes)+"s",bg="white",width=25,relief="groove",font=self.font)
        if (self.sec > 0):
            self.after(1000,self.chrono)

    def login(self):
        user_answer = self.remove_accents(self.entry_pwd.get())
        s_pwd = self.remove_accents(pwd)
        if user_answer.lower() == s_pwd.lower():
            self.initialize()
        else:
            self.lbl_login_ko.configure(text='wrong identifier', state='normal')
        return
    
    def reset_doc(self):
        f = open("input_badge.txt", "w")
        f.write('')
        f.close()
        f = open("init.txt", "w")
        f.write('')
        f.close()
        
    def pre_initialize(self):
        self.reset_doc()
        
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
        self.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12),weight=1)
        self.lempty = Label(self, text="", padx=200, pady=200).grid(row=0, column=0, sticky='nsew')
        self.lempty2 = Label(self, text="", padx=200, pady=200).grid(row=0, column=10, sticky='nsew')
        self.lempty3 = Label(self, text="", padx=200, pady=200).grid(row=10, column=0, sticky='nsew')
        self.lempty4 = Label(self, text="", padx=200, pady=200).grid(row=10, column=10, sticky='nsew')

        self.running_game1 = 0
        self.running_game3 = 0
        self.running_game4 = 0

        self.font = "-family {Helvetica} -size -20 -weight bold"
        self.lbl = Label(self, text="User:", relief='groove', padx=25, width=9)
        self.lbl.configure(font=self.font)
        self.lbl.grid(row=1, column=1, columnspan=2)
        
        self.entry_login = Entry(self)#, width=50)
        self.entry_login.insert(0,'PereNoel')
        self.entry_login.configure(state='disabled', font=self.font)
        self.entry_login.grid(row=1, column=2, columnspan=3)

        self.lbl_pwd = Label(self, text="Password:", relief='groove', padx=25, width=9)
        self.lbl_pwd.configure(font=self.font)
        self.lbl_pwd.grid(row=2, column=1, columnspan=2)
        
        self.entry_pwd = Entry(self, show='*', font=self.font)#, width=50)
        self.entry_pwd.grid(row=2, column=2, columnspan=3)
        
        self.btn_Ok = Button(self, text="Ok", command=self.login, font=self.font)
        self.btn_Ok.grid(row=3, column=1, columnspan=2)
        
        self.btn_Cancel = Button(self, text="Cancel", state='disabled', font=self.font)
        self.btn_Cancel.grid(row=3, column=2, columnspan=2)
        
        self.btn_Forget = Button(self, text="Password Forgotten ?", command=self.ForgetPwd, font=self.font)
        self.btn_Forget.grid(row=3, column=4, columnspan=2)

        self.lbl_login_ko = Label(text="", font=self.font)
        self.lbl_login_ko.configure(state='disabled')
        self.lbl_login_ko.grid(row=4, column=2, columnspan=3)
        
        if debug == 'true':
            button = Button(self, text="Debug_Quit", command=self.destroy)
            button.grid(row=11, column=3)

        #Timer:
        start_s = remaining_time
        start_m = int(remaining_time / 60)
        start_s %= 60
        self.textTime = Label(self, text="Time remaining: "+str(start_m)+"min "+str(start_s)+"s",bg="white",width=25,relief="groove",font=self.font)
        self.textTime.grid(row=10, column=1, columnspan=4)
        self.chrono()

    def UnlcokDesk(self):
        self.buttonGame1.config(text="Santa\'s Office\n\nUnlocked", bg='green',font=self.font)
        subprocess.call("./lightOff.sh", shell=True)
        
    def initialize(self):
        self.clear()
        
        #Game1:
        global buttonGame1
        self.buttonGame1 = Button(self,text="Santa\'s Office\n\nLocked", bg='red', width=15,height=5, command=self.UnlcokDesk,font=self.font)
        self.buttonGame1.grid(row=1, column=1, columnspan=1)
        textGame1 = Label(self, text="", state="disabled").grid(row=2, column=1)

        #Game2:
        self.buttonGame2 = Button(self,text='Wallpaper', bg='grey', width=15,height=5,command=self.ShowWallpaper,font=self.font)
        self.buttonGame2.grid(row=1, column=3)
  
        #Game3:
        self.buttonGame3 = Button(self,text='Security Camera', bg='grey', width=15,height=5,command=self.SecurityCam,font=self.font)
        self.buttonGame3.grid(row=3, column=1)
        textGame3 = Label(self, text="", state="disabled").grid(row=2, column=2)

        #Game4:
        self.buttonGame4 = Button(self,text="Disengage \nLockdown",bg='red', width=15,height=5,command=self.DisengageLockdown,font=self.font)
        self.buttonGame4.grid(row=3, column=3)
        textGame4 = Label(self, text="", state="disabled").grid(row=4, column=2)

        #self.grid_columnconfigure(0,weight=1)
        #self.grid_columnconfigure(7,weight=1)
        #self.grid_rowconfigure(0,weight=1)
        #self.grid_rowconfigure(7,weight=1)
        #self.resizable(False,False)
        
        #Timer:
        #start_s = remaining_time
        #start_m = int(remaining_time / 60)
        #start_s %= 60
        #self.textTime = Label(self, text="Time remaining: "+str(start_m)+"min "+str(start_s)+"s",bg="white",width=25,relief="groove",font=self.font)
        #self.textTime.grid(row=6, column=1, columnspan=4)


    def clear(self):      
        self.lbl.destroy()
        self.entry_login.destroy()
        self.btn_Ok.destroy()
        self.btn_Cancel.destroy()
        self.btn_Forget.destroy()
        self.lbl_pwd.destroy()
        self.entry_pwd.destroy()
        self.lbl_login_ko.destroy()

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
    
    def ForgetPwd(self):
        if self.running_game1 == 0:
            self.running_game1 = 1
            g1.main()
            if self.test_game(1) == 'true':
                if debug=='true':print("jeu 1 ok")
            else:
                self.running_game1 = 0
        else:
            return
         
    def ShowWallpaper(self):
        self.top = Toplevel()
        self.top.focus_force()
        self.top.grab_set()
        self.top.resizable(False,False)

        can1 = Canvas(self.top, width = 550, height = 428, bg = 'white')
        p = PhotoImage(file='papanowel.gif')
        item = can1.create_image(250, 228, image=p)
        can1.image = p
        can1.grid()

    def LimitSizeEntry(self,*args):
        value = self.CodeValue.get()
        if len(value) > 1:self.CodeValue.set(value[:1])
        value2 = self.CodeValue2.get()
        if len(value2) > 1:self.CodeValue2.set(value2[:1])
        value3 = self.CodeValue3.get()
        if len(value3) > 1:self.CodeValue3.set(value3[:1])
        value4 = self.CodeValue4.get()
        if len(value4) > 1:self.CodeValue4.set(value4[:1])
        
    def SecurityCam(self):
        if self.running_game3 == 0:
            self.running_game3 = 1
            self.top = Toplevel(self)
            self.top.protocol('WM_DELETE_WINDOW', lambda: None)
            self.top.focus_force()
            self.top.grab_set()
            self.top.geometry("300x100")
            self.top.resizable(False,False)
            self.top.grid_rowconfigure((0,1,2,3,4),weight=1)
            self.top.grid_columnconfigure((0,1,2,3,4),weight=1)

            self.top.lbl_empty = Label(self.top, text='', width=30)
            self.top.lbl_empty.grid(row=4, column=2, columnspan=3)
            
            self.CodeValue = StringVar()
            self.CodeValue.trace('w', self.LimitSizeEntry)
            self.CodeValue2 = StringVar()
            self.CodeValue2.trace('w', self.LimitSizeEntry)
            self.CodeValue3 = StringVar()
            self.CodeValue3.trace('w', self.LimitSizeEntry)
            self.CodeValue4 = StringVar()
            self.CodeValue4.trace('w', self.LimitSizeEntry)
            
            self.top.btn1 = Button(self.top, text='Ok', command=self.Show_SecurityCam,font=self.font)
            self.top.btn1.grid(row=2, column=1, columnspan=2)

            self.top.btn2 = Button(self.top, text='Quit', command=self.close_SecurityCam,font=self.font)
            self.top.btn2.grid(row=2, column=2, columnspan=2)

            self.top.ent1 = Entry(self.top, width=4, bg='white', textvariable=self.CodeValue,font=self.font)
            self.top.ent1.grid(row=1, column=1)
            
            self.top.ent2 = Entry(self.top, width=4, bg='white', textvariable=self.CodeValue2,font=self.font)
            self.top.ent2.grid(row=1, column=2)
            
            self.top.ent3 = Entry(self.top, width=4, bg='white', textvariable=self.CodeValue3,font=self.font)
            self.top.ent3.grid(row=1, column=3)
            
            self.top.ent4 = Entry(self.top, width=4, bg='white', textvariable=self.CodeValue4,font=self.font)
            self.top.ent4.grid(row=1, column=4)

            self.top.lbl = Label(self.top, text='Is your \'phone connected\' ?', width=30,font=self.font)
            self.top.lbl.grid_remove()
            self.top.bindic = Button(self.top, bitmap='question',command=lambda:self.top.lbl.grid(row=4, column=1, columnspan=3),font=self.font)
            self.top.bindic.grid(row=2, column=3, columnspan=2)

    def close_SecurityCam(self):
        self.running_game3 = 0
        self.top.destroy()
        
    def Show_SecurityCam(self):
        if (self.top.ent1.get() == str(2)) and (self.top.ent2.get() == str(8)) and (self.top.ent3.get() == str(9)) and (self.top.ent4.get() == str(4)):
            self.top.lbl.destroy()
            self.top.lbl_end = Label(self.top, text='video link ?', width=30,font=self.font)
            self.top.lbl_end.grid(row=4, column=1, columnspan=3)
            self.top.ent1.configure(state='disabled')
            self.top.ent2.configure(state='disabled')
            self.top.ent3.configure(state='disabled')
            self.top.ent4.configure(state='disabled')
            self.buttonGame3.config(text="Security Camera", bg='green',font=self.font)
            #TODO ajouter lien vidéo
            f = open("init.txt", "a")
            line = "finish_game3\n"
            f.write(line)
            f.close()
            return
        else:
            self.running_game3 = 0
            
    
    def DisengageLockdown(self):
        g4.main()


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Escape Game Conti')
    app.attributes('-fullscreen', 1)
    #app.geometry("250x350")
    subprocess.call("./lightOn.sh", shell=True)
    app.mainloop()
