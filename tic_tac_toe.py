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

#customize the window
def Gui():
  Iamage = PhotoImage(file="tct.png")
  Window.iconphoto(True, Iamage)
  Window.title("Tic Tac Toe")


Gui()
#randomly choose the first player
players = ["X","O"]
player = random.choice(players)

#list of buttons
buttuns = [["0","0","0"],
           ["0","0","0"],
           ["0","0","0"]]

#adding buttons to the window
butframe = Frame(Window)
butframe.pack(side=BOTTOM)

for row in range(3):
    for col in range(3):
        buttuns[row][col] = Button(butframe, text="", font=("consoles",40), width=5, height=3,
                                  command=lambda r=row, c=col: next_turn(r, c))
        buttuns[row][col].grid(row=row, column=col)




#whos turn is know?
txt_lable = Label(Window, text=f"{player} turn", font=("consoles",40))
txt_lable.pack(side=TOP)


#reset buttun 
reset_buttun = Button(text="restart", font=("consoles",20), command=new_game)
reset_buttun.pack(side=TOP)







Window.mainloop()


