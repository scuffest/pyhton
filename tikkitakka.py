from tkinter import *
from tkinter import messagebox
import random

# Funktion som hanterar spelarens drag
def next_turn(row, column):
    global player  # Använder global player för att hålla reda på aktuell spelare

    # Kontrollera om rutan är tom och om det inte finns någon vinnare
    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player  # Sätt spelarens symbol i rutan alltså X eller O

        #ser till om någon vinner eller om det är oavgjort
        if check_winner():
            label.config(text=f"{player} wins")
        elif check_tie():
            label.config(text="Tie!")
        else:
            # Byt spelare
            player = players[1] if player == players[0] else players[0]
            label.config(text=f"{player} turn")
    else:
        # Om någon trycker på en ruta som är redan använt så kommer ett tkiner messagebox poppa upp och säga att rutan är redan använt.
        messagebox.showerror("Fel", "Rutan har redan använts, välj en annan ruta")

# Kollar igenom vem som van
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

# För att se till om det är oavgjord
def check_tie():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                return False
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(bg="yellow")
    return True

# Startar ett nytt spel därför heter den "new_game"
def new_game():
    global player
    player = random.choice(players)  # Väljer en random spelare
    label.config(text=f"{player} turn")  # Uppdatera etiketten

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")  # Restartar knapparna

# skapa huvudfönstret för spelet
window = Tk()
window.title("Tikki-Takka")

# Definiera spelarna och välj en slumpmässig spelare
players = ["x", "o"]
player = random.choice(players)

# Skapa etiketten som visar vems tur det är, Label är en sak i Tkinter som används för att visa exempelvis text eller bilder text=f"{player} 
#turn" anger texten som ska visas i etiketten, font=('consolas', 40) anger teckensnittet ('consolas') och teckenstorleken (40)
label = Label(text=f"{player} turn", font=('consolas', 40))
# pack används för att placera etiketten i fönstret
label.pack(side="top")

# Skapa en knapp för att starta om spelet
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Detta skapar en frame alltså en ram 
frame = Frame(window)
frame.pack()

# Skapa en 2D-lista för knapparna
buttons = [[None for _ in range(3)] for _ in range(3)]

# For in range skapar knappar och placerar dem i ramen och gör det till en rutnät
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                   # lambda används för att skapa en anonym funktion
                                   # lambda används här för att skicka specifika argument alltså (row och col) till next_turn
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

# Detta är mainloopen utan den är det lite svårare att använda tkinter har jag märkt.
window.mainloop()
