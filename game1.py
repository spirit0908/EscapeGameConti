from tkinter import *
import unicodedata

solution_step1 = 'kinder'
solution_step2 = 'le pere noel est une ordure'
solution_step3 = 'Comète'
solution_step4 = 'Cookies'
Font_lbl = "-family {Helvetica} -size -20 -weight bold"

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def step1(master_g1,entry1):
    user_answer = remove_accents(entry1.get())
    s_step1 = remove_accents(solution_step1)
    if user_answer.lower() == s_step1:
        label2 = Label(master_g1, text="Well done !                ", font=Font_lbl)
        label2.grid(row=1, column=0, columnspan=3)
        entry1.config(state="disabled")
        step2(master_g1)
    else:
        label2 = Label(master_g1, text="Wrong answer", font=Font_lbl)
        label2.grid(row=1, column=0, columnspan=3)
    
def step2(master_g1):
    label3 = Label(master_g1, text="What movie do you hate the most ?", font=Font_lbl)
    label3.grid(row=3, column=0)
    entry2 = Entry(master_g1, width=25, font=Font_lbl)
    entry2.grid(row=3, column=1, columnspan=3)
    button2 = Button(master_g1,text="Ok", command=lambda:answer_step2(master_g1,entry2), font=Font_lbl).grid(row=3,column=4, columnspan=1)

def answer_step2(master_g1, entry2):
    user_answer = remove_accents(entry2.get())
    s_step2 = remove_accents(solution_step2)
    if user_answer.lower() == s_step2.lower():
        label4 = Label(master_g1, text="Well done !                ", font=Font_lbl)
        label4.grid(row=4, column=0, columnspan=3)
        entry2.config(state="disabled")
        step3(master_g1)
    else:
        label4 = Label(master_g1, text="Wrong answer", font=Font_lbl)
        label4.grid(row=4, column=0, columnspan=3)

def step3(master_g1):
    label5 = Label(master_g1, text="Who is the reindeer of the month ?", font=Font_lbl)
    label5.grid(row=5, column=0)
    entry3 = Entry(master_g1, width=25, font=Font_lbl)
    entry3.grid(row=5, column=1, columnspan=3)
    button3 = Button(master_g1,text="Ok", command=lambda:answer_step3(master_g1,entry3), font=Font_lbl).grid(row=5,column=4, columnspan=1)

def answer_step3(master_g1, entry3):
    user_answer = remove_accents(entry3.get())
    s_step3 = remove_accents(solution_step3)
    if user_answer.lower() == s_step3.lower():
        label6 = Label(master_g1, text="Well done !                ", font=Font_lbl)
        label6.grid(row=6, column=0, columnspan=3)
        entry3.config(state="disabled")
        step4(master_g1)
    else:
        label6 = Label(master_g1, text="Wrong answer", font=Font_lbl)
        label6.grid(row=6, column=0, columnspan=3)

def step4(master_g1):
    label7 = Label(master_g1, text="What is you favorite dish ?", font=Font_lbl)
    label7.grid(row=7, column=0)
    entry4 = Entry(master_g1, width=25, font=Font_lbl)
    entry4.grid(row=7, column=1, columnspan=3)
    button4 = Button(master_g1,text="Ok", command=lambda:answer_step4(master_g1,entry4), font=Font_lbl).grid(row=7,column=4, columnspan=1)

def answer_step4(master_g1, entry4):
    user_answer = remove_accents(entry4.get())
    s_step4 = remove_accents(solution_step4)
    if user_answer.lower() == s_step4.lower():
        label8 = Label(master_g1, text="Well done !                ")
        label8.grid(row=8, column=0, columnspan=3)
        entry4.config(state="disabled")
        game1_end(master_g1)
    else:
        label8 = Label(master_g1, text="Wrong answer")
        label8.grid(row=8, column=0, columnspan=3)

def game1_end(master_g1):
    label9 = Label(master_g1, text="Welcome Santa ! Good to see you again.", font=Font_lbl)
    label9.grid(row=8, column=0, columnspan=3)
    label10 = Label(master_g1, text="Your new password is: SwoftwarePlatform", font=Font_lbl)
    label10.grid(row=9, column=0, columnspan=3)
    button5 = Button(master_g1,text="Finish", command=lambda:close(master_g1), font=Font_lbl).grid(row=10,column=1, columnspan=1)

def close(master_g1):
    f = open("init.txt", "a")
    line = "finish_game1\n"
    f.write(line)
    f.close()
    master_g1.destroy()

def main():
    ### Main ###
    master_g1 = Tk()
    master_g1.title('Recover password')
    master_g1.geometry("750x550")
    master_g1.protocol('WM_DELETE_WINDOW', lambda: None)
    master_g1.columnconfigure(0, weight=3)
    master_g1.columnconfigure(1, weight=2)
    master_g1.columnconfigure(2, weight=1)
    ## Login ##
    label1 = Label(master_g1, text="What is your favorite chocolate ?", font=Font_lbl)
    label1.grid(row=0, column=0)
    entry1 = Entry(master_g1, width=25, font=Font_lbl)
    entry1.grid(row=0, column=1, columnspan=3)

    button1 = Button(master_g1,text="Ok", command=lambda:step1(master_g1, entry1), font=Font_lbl).grid(row=0, column=4,columnspan=1)

    #game1_end(master_g1)

    master_g1.mainloop()
