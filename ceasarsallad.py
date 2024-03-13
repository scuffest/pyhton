meddelande = input("Vill du dekryptera eller inkryptera?")

alfabetet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
print()

def dekrypt():
 dek = input("Text du vill dekryptera och key")
 dek_split = dek.split()
 print(dek_split)

def inkrypt():
 print("")

if meddelande == "dekryptera":
 dekrypt(meddelande)