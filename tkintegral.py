import tkinter as tk

# Skapa huvudfönstret
root = tk.Tk()
root.title("Min första Tkinter-applikation")

# Skapa en etikett
label = tk.Label(root, text="Välkommen till Tkinter!")
label.pack()

# Skapa en inmatningsruta
inmatning = tk.Entry(root)
inmatning.pack()

# Funktion för att hämta text från inmatningsrutan
def hamta_text():
    text = inmatning.get()
    label.config(text="Hej " + text)

# Skapa en knapp för att hämta text
text_knapp = tk.Button(root, text="Hämta text", command=hamta_text)
text_knapp.pack()

# Starta huvudloopen
root.mainloop()
