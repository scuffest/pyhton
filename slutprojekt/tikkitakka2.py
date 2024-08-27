# Importera Tkinter-modulen för GUI och random-modulen för att välja spelare slumpmässigt
from tkinter import *
from tkinter import messagebox
import random

# Funktionen next_turn hanterar vad som händer när en spelare tar sitt drag
def next_turn(row, column):
    global player  # Använd den globala variabeln 'player' för att hålla reda på vem som är nuvarande spelare

    # Kontrollera om den valda rutan är tom och om det inte finns någon vinnare ännu
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # Om nuvarande spelare är den första spelaren i listan 'players'
        if player == players[0]:

            # Sätt spelarens symbol i den valda rutan
            buttons[row][column]['text'] = player

            # Om det inte finns någon vinnare, byt till nästa spelare
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            # Om det finns en vinnare, visa att den första spelaren vinner
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            # Om det är oavgjort, visa "Tie!"
            elif check_winner() == "Tie":
                label.config(text="Tie!")

        # Om nuvarande spelare inte är den första spelaren i listan
        else:

            # Sätt spelarens symbol i den valda rutan
            buttons[row][column]['text'] = player

            # Samma kontroller som ovan men för den andra spelaren
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")
    else:
        # Om rutan redan är använd, visa ett felmeddelande
        messagebox.showerror("Fel", "Rutan har redan använts, välj en annan ruta")

# Funktionen check_winner kontrollerar om det finns en vinnare
def check_winner():
    # Kontrollera varje rad för seger
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            # Ändra färgen på de vinnande knapparna till grönt
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Kontrollera varje kolumn för seger
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Kontrollera diagonalerna för seger
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # Om det inte finns några tomma rutor och ingen vinnare, är det oavgjort
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

# Funktionen empty_spaces kontrollerar om det finns några tomma rutor kvar
def empty_spaces():
    spaces = 9  # Börja med att anta att alla 9 rutor är tomma

    # Räkna ner för varje ruta som inte är tom
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    # Om det inte finns några tomma rutor kvar, returnera False
    if spaces == 0:
        return False
    else:
        return True

# Funktionen new_game startar ett nytt spel
def new_game():
    global player  # Använd den globala variabeln 'player'

    # Välj en slumpmässig spelare för att börja spelet
    player = random.choice(players)

    # Uppdatera etiketten för att visa vems tur det är
    label.config(text=player + " turn")

    # Återställ alla knappar till deras ursprungliga tillstånd
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Skapa huvudfönstret för spelet och sätt titeln
window = Tk()
window.title("Tic-Tac-Toe")

# Definiera spelarna och välj en slumpmässig spelare för att börja
players = ["x", "o"]
player = random.choice(players)

# Skapa en 2D-lista för att hålla reda på knapparna i spelet
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Skapa en etikett för att visa vems tur det är
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

# Skapa en knapp för att starta om spelet
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Skapa en ram för att organisera knapparna
frame = Frame(window)
frame.pack()

# Skapa knapparna och placera dem i ett rutnät
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Starta huvudloopen för att visa fönstret och börja spelet
window.mainloop()
