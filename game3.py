from tkinter import *
import unicodedata
#from EscapeGameConti import *

solution_step1 = 'merry'
solution_step2 = 'christmas'

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def step1(master_g2,entry1,entry2):
    user_answer = remove_accents(entry1.get())
    s_step1 = remove_accents(solution_step1)
    user_answer2 = remove_accents(entry2.get())
    s_step2 = remove_accents(solution_step2)
    label5 = Label(master_g2)
    if (user_answer.lower() == s_step1) and (user_answer2.lower() == s_step2):
        label5.config(text='Your desk is now unlocked')
        label5.grid(row=4, column=0, columnspan=3)
        entry1.config(state="disabled")
        entry2.config(state="disabled")
        game2_end(master_g2)
    else:
        label5.config(text="Wrong answer")
        label5.grid(row=4, column=0, columnspan=3)

def game2_end(master_g2):
    label10 = Label(master_g2, text="You can click on \"Finish\"")
    label10.grid(row=8, column=0, columnspan=3)
    button5 = Button(master_g2,text="Finish", command=lambda:close(master_g2)).grid(row=10,column=1, columnspan=1)

def close(master_g2):
    f = open("init.txt", "a")
    line = "finish_game2\n"
    f.write(line)
    f.close()
    master_g2.destroy()

def main():
    ### Main ###   
    master_g2 = Tk()
    master_g2.title('Unlock Santa\'s office')
    master_g2.geometry("550x250")

    master_g2.columnconfigure(0, weight=3)
    master_g2.columnconfigure(1, weight=2)
    master_g2.columnconfigure(2, weight=1)
    ## Question ##
    label1 = Label(master_g2, text="13-8+13+0+7")
    label1.grid(row=0, column=0)
    label3 = Label(master_g2, text="_ _ _ _ _")
    label3.grid(row=0, column=1)
    entry1 = Entry(master_g2, width=50)
    entry1.grid(row=0, column=2)

    label2 = Label(master_g2, text="3+5+10-9+10+1-7-12+18")
    label2.grid(row=2, column=0)
    label4 = Label(master_g2, text="_ _ _ _ _ _ _ _ _")
    label4.grid(row=2, column=1)
    entry2 = Entry(master_g2, width=50)
    entry2.grid(row=2, column=2)

    button1 = Button(master_g2,text="Validate", command=lambda:step1(master_g2,entry1,entry2)).grid(row=3, column=1,columnspan=1)

    #game1_end(master_g2)

    master_g2.mainloop()
