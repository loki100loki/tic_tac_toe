from tkinter import *
import random


def next_turn(row, col):
    global player
    if buttuns[row][col][Text] == "" and check_winer() is False:
        if player == players[0]:
            buttuns[row][col]["text"]= player


            if check_winer() is False:
                player = players[1]
                txt_lable.config(text=(players[1] + " turn"))
            elif check_winer() is True:
                txt_lable.config(text=(players[0] + " win"))
            elif empty_spaces() is False:
                txt_lable.config(text="its a tie!")
        else:
            buttuns[row][col]["text"]= player


            if check_winer() is False:
                player = players[0]
                txt_lable.config(text=(players[0] + " turn"))
            elif check_winer() is True:
                txt_lable.config(text=(players[1] + " win"))
            elif empty_spaces() is False:
                txt_lable.config(text="its a tie!")
       
            


    pass


def check_winer():
    if buttuns[row][0]["text"]==buttuns[row][1]["text"]==buttuns[row][2]["text"]!="":
        return True
    elif buttuns[0][col]["text"]==buttuns[1][col]["text"]==buttuns[2][col]["text"]!="":
        return True
    elif buttuns[0][0]["text"]==buttuns[1][1]["text"]==buttuns[2][2]["text"]!="":
        return True
    elif buttuns[0][2]["text"]==buttuns[1][1]["text"]==buttuns[2][0]["text"]!="":
        return True
    elif empty_spaces() is False:
        return None
    else:
        return False


        

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
                                  command=lambda row=row, col=col: next_turn(row,col))
        buttuns[row][col].grid(row=row, column=col)




#whos turn is know?
txt_lable = Label(Window, text=f"{player} turn", font=("consoles",40))
txt_lable.pack(side=TOP)


#reset buttun 
reset_buttun = Button(text="restart", font=("consoles",20), command=new_game)
reset_buttun.pack(side=TOP)







Window.mainloop()


