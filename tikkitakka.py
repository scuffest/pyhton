# Importera nödvändiga moduler från Tkinter och random
from tkinter import *
from tkinter import messagebox
import random

# Funktion som hanterar spelarens drag
def next_turn(row, column):
    global player  # Använd global variabel 'player' för att hålla reda på aktuell spelare

    # Kontrollera om rutan är tom och om det inte finns någon vinnare
    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player  # Sätt spelarens symbol i rutan

        # Kontrollera om någon vinner eller om det är oavgjort
        if check_winner():
            label.config(text=f"{player} wins")
        elif check_tie():
            label.config(text="Tie!")
        else:
            # Byt spelare
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} turn")
    else:
        # Visa felmeddelande om rutan redan är använd
        messagebox.showerror("Fel", "Rutan har redan använts, välj en annan ruta")

# Funktion som kontrollerar om någon vinner
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            for col in range(3):
                buttons[row][col].config(bg="green")
            return True

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            for row in range(3):
                buttons[row][col].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        for i in range(3):
            buttons[i][i].config(bg="green")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        for i in range(3):
            buttons[i][2-i].config(bg="green")
        return True

    return False

# Funktion som kontrollerar om spelet är oavgjort
def check_tie():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return False
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(bg="yellow")
    return True

# Funktion som startar ett nytt spel
def new_game():
    global player
    player = random.choice(players)  # Välj en slumpmässig spelare
    label.config(text=f"{player} turn")  # Uppdatera etiketten

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")  # Återställ alla knappar

# Skapa huvudfönstret för spelet
window = Tk()
window.title("Tic-Tac-Toe")

# Definiera spelarna och välj en slumpmässig spelare
players = ["x", "o"]
player = random.choice(players)

# Skapa etiketten som visar vems tur det är
# Label är en widget i Tkinter som används för att visa text eller bilder
# text=f"{player} turn" anger texten som ska visas i etiketten
# font=('consolas', 40) anger teckensnittet ('consolas') och teckenstorleken (40)
label = Label(text=f"{player} turn", font=('consolas', 40))
# pack används för att placera etiketten i fönstret
label.pack(side="top")

# Skapa en knapp för att starta om spelet
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Skapa en ram för knapparna
frame = Frame(window)
frame.pack()

# Skapa en 2D-lista för knapparna
buttons = [[None for _ in range(3)] for _ in range(3)]

# Skapa knapparna och placera dem i ett rutnät
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                   # lambda används för att skapa en anonym funktion
                                   # Här används lambda för att skicka specifika argument (row och col) till next_turn
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

# Starta huvudloopen för att visa fönstret och börja spelet
window.mainloop()
