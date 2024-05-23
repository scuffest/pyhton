import tkinter as tk

# Skapa huvudfönstret
root = tk.Tk()
root.title("Hälsningar")
root.geometry("450x250")
root.configure(bg="pink")
# Skapa en etikett
label = tk.Label(root, text="Ange ditt namn!", fg="white", bg="pink")
label.pack()

# Skapa en inmatningsruta
inmatning = tk.Entry(root)
inmatning.pack()

# Funktion för att hämta text från inmatningsrutan
def hamta_text():
    text = inmatning.get()
    label.config(text="Hej " + text, bg="pink")

# Skapa en knapp för att hämta text
text_knapp = tk.Button(root, text="Klicka här", command=hamta_text, fg="white", bg="pink")
text_knapp.pack()

# Starta huvudloopen
root.mainloop()
