from tkinter import *
import tkinter as tk
import random
import time
from time import strftime

my_root = tk.Tk()
my_root.geometry("600x600")
my_root.title("Typing Test")
my_root.config(bg="black")

text1 = "When he burned, she watched from the window as the casket \nshifted toward the chamber, as the cardboard lid vibrated, \nshuddered apart at the seam to reveal his hands, \na moment before they would blossom in the fire \nthat reflected in the metal frame of the door, \nthe bloom that would arc in delicate peels." 
text2 = "There are bees trapped into the walls of an abandoned home.\n There are ghosts trapped in the attic, swaying to their hum.\n There are flies trapped on a glue strip, beating their wings in anger. \nThere’s a girl in the kitchen, trying to release them. \nShe pulls the flies transparent wings, they come off in her fingers." 
text3 = "A wonderful serenity has taken possession of my entire soul, \nlike these sweet mornings of spring which I enjoy with my whole heart.\n I am alone, and feel the charm of existence in this spot, \nwhich was created for the bliss of souls like mine. \nI am so happy, my dear friend, so absorbed \nin the exquisite sense of mere tranquil existence."
text4 = "An aggressive alien creature visited our planet.\n It was ugly, with a big nose, pinkish hairy skin, and feet that smelled.\nIt was frightened of us for no reason. \nIt resented our differences. \nIt laid claim to our planet.\nThis strange alien was an Earth Human. \nIt called me ALIEN."

txt_lst = [text1,text2,text3,text4]

#def submit():

def logic():
    now = strftime("%H %M %S")
    lst = list(now.split())
    sec = int(lst[0])*3600 + int(lst[1])*60 + int(lst[2])

    txt = random.choice(txt_lst)
    t_lst = txt.split()
    
    l1 = Label(my_root, text = "Welcome to Typing Test", bg ="black", fg = "cyan")
    l1.config(font=("Arial",20,"bold italic"))
    l1.pack(pady=5)
    
    f1 = Frame(my_root,bg="white")
    f1.pack(pady=30)

    l2 = Label(f1, text = txt, fg= "yellow", bg="black")
    l2.config(font=("Arial",10,"bold italic"))
    l2.pack(padx=3,pady=3)

    e1 = tk.Entry(my_root)
    e1.config(width=80)
    e1.pack(ipady=35)

    f2 = Frame(my_root,bg = "black")
    f2.pack(pady =20)

    def submit():
        c_er = 0
        err_lst=[]
        n_now = strftime("%H %M %S")
        lst1 = list(n_now.split())
        sec1 = int(lst1[0])*3600 + int(lst1[1])*60 + int(lst1[2])
        diff = sec1 - sec

        inp = e1.get()
        inp_lst = inp.split()
        
        wpm= int((len(inp_lst)/int(diff))*60)

        spdl = Label(f2, text = "Your current speed is : "+str(wpm)+"wpm", bg= "black", fg = "yellow")
        spdl.config(font = ("Arial",15,"bold"))
        spdl.pack()
        
        for i in range(0,len(inp_lst)):
            if inp_lst[i] != t_lst[i]:
                c_er +=1
                err_lst.append(inp_lst[i])
                
        cerl = Label(f2, text = "You have made "+str(c_er)+" errors",bg = "black", fg = "yellow")
        cerl.config(font = ("Arial",15,"bold"))
        cerl.pack()

        if len(err_lst)>0:
            erl = Label(f2, text = "The errors are : "+str(err_lst)+".",bg = "black", fg = "yellow")
            erl.config(font = ("Arial",15,"bold"))
            erl.pack()
        
        
    
    b1 = Button(my_root, text = "Submit",command = submit, fg="black", bg ="yellow")
    b1.pack(side = LEFT, padx =100)
    
    def restart():
        l1.destroy()
        f1.destroy()
        f2.destroy()
        e1.destroy()
        b1.destroy()
        b2.destroy()
        logic()

    b2 = Button(my_root, text = "Restart", command = restart, fg="black", bg ="yellow")
    b2.pack(side = RIGHT, padx =100)
                
logic()
my_root.mainloop()
