from os import system
from tkinter import *
from typing import Tuple
import dat
from tkinter.ttk import Combobox
import sys
window = Tk()
characters = []
ryuk = dat.character("ryuk","Рьюк")
light = dat.character("light","Ягами Лайт")
l = dat.character("l","L")
misa = dat.character("misa","Амана Миса")
watari = dat.character("watari","Ватари")
raye = dat.character("raye", "Рэй Пэмбэр")
rem = dat.character("rem", "Рэм")
soichiro = dat.character("soichiro", "Ягами Соитиро")
characters.append(ryuk)
characters.append(light)
characters.append(l)
characters.append(misa)
characters.append(watari)
characters.append(raye)
characters.append(rem)
characters.append(soichiro)
def find_char(nam : str) -> dat.character:
    for c in characters:
        if c == nam:
            return c

def pick_char(e):
    global new_photo
    global new_photo2
    global text
    global dropdown
    char = find_char(dropdown.get())
    text.configure(text=char.description)
    print(char.prim_img)
    new_photo = PhotoImage(file=char.prim_img)
    new_photo2 = None
    if char.sec_img != None:
        new_photo2 = PhotoImage(file=char.sec_img)
        panel2.config(image=new_photo2)
    panel.config(image=new_photo,width=500,height=500)
    panel.grid(column=1,row=1)


photo1 = PhotoImage(file="")
photo2 = PhotoImage(file="")
button = Button(window,text="Закрыть программу", width=20, height=2)
button.bind("<Button-1>",lambda e: sys.exit(0))
button.grid(row=0,column=0)
dropdown = Combobox(window)
dropdown["values"] = dropdown["values"] + "Рьюк", "Амана Миса", "L", "Ягами Лайт", "Рэй Пэмбэр", "Рэм", "Ягами Соитиро", "Ватари"


dropdown.grid(column=0,row=1)




panel = Label(window,image=photo1, width=500,height=500)
panel.grid(column=1,row=1)
panel2 = Label(window,image=photo2, width=500,height=500)
panel2.grid(column=2,row=1) 
text = Label(text="", width=100, font="Arial 12")
text.grid(column=1,columnspan=2,row=2)

dropdown.bind("<<ComboboxSelected>>",pick_char)



window.mainloop()