from tkinter import *
import random

# --- Functions ---

def next_turn(row, col):
    global player
    if buttons[row][col]['text'] == "" and check_winner() is False:
        buttons[row][col]['text'] = player

        winner = check_winner()

        if winner is False:
            # Switch turn
            player = players[1] if player == players[0] else players[0]
            txt_label.config(text=f"{player} turn")
        elif winner == "Tie":
            txt_label.config(text="It's a tie!")
        else:
            txt_label.config(text=f"{player} wins!")

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for col in range(3):
                buttons[row][col].config(bg="green")
            return True

    # Check columns
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            for row in range(3):
                buttons[row][col].config(bg="green")
            return True

    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    if empty_spaces() is False:
        # Tie
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"

    return False

def empty_spaces():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    txt_label.config(text=f"{player} turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")

# --- Main Window ---
window = Tk()
window.title("Tic Tac Toe")

# Set icon
try:
    icon_img = PhotoImage(file="tct.png")
    window.iconphoto(True, icon_img)
except:
    pass  # If the icon file doesn't exist, continue

# --- Players ---
players = ["X", "O"]
player = random.choice(players)

# --- Buttons Grid ---
buttons = [[0 for _ in range(3)] for _ in range(3)]
frame = Frame(window)
frame.pack(side=BOTTOM)

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                   command=lambda r=row, c=col: next_turn(r, c))
        buttons[row][col].grid(row=row, column=col)

# --- Turn Label ---
txt_label = Label(window, text=f"{player} turn", font=("consolas", 40))
txt_label.pack(side=TOP)

# --- Restart Button ---
reset_button = Button(window, text="Restart", font=("consolas", 20), command=new_game)
reset_button.pack(side=TOP)

window.mainloop()
