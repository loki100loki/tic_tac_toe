from tkinter import *
import random


def next_turn():
    pass


def check_winer():
    pass

def empty_spaces():
    pass

def new_game():
    pass


Window = Tk()
def Gui():
  Iamage = PhotoImage(file="tct.png")
  Window.iconphoto(True, Iamage)
  Window.title("Tic Tac Toe")
  Window.geometry("400x400")

Gui()

players = ["X","O"]

player = random.choice(players)
buttuns = [["0","0","0"],
           ["0","0","0"],
           ["0","0","0"]]


txt_lable = Label(text=f"now is {player} turn", font=("consoles",40))
txt_lable.pack(side=TOP)

reset_buttun = Button(text="restart", font=("consoles",20), command=new_game)
reset_buttun.pack(side=TOP)







Window.mainloop()


