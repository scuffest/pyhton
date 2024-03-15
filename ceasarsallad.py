import random

def kryptering(nyckel, meddelande):
# Funktion för kryptering och dekryptering, med två listor där jag har storaalfabeter och det lilla. Jag gör detta ifall användaren väljer att skriva allting i storabokstäver eller i små eller blandat.
  alfabetet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
  storaalfabetet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]
  hej = ""        # hej = "" i koden är för vad text ska läggas in därför skrivs det hej += krypterad för vi lägger det krypterade meddelandet i hej.
# Den går in i mitt for loop då jag använder .isupper för storaalfabetet och .islower för alfabetet sedan else är ifall användaren väljer att skriva ett mellanrum i deras meddelande.
  for character in meddelande:
    if character.isupper():
      bokstav =   (storaalfabetet.index(character)  +nyckel)   % 28   # Jag använder index för att ta reda på vilken int en bokstav ligger på i listan sedan så adderas den med för vilken nyckel använadren skrev för att ta reda på hur många steg den ska hoppa fram i listan.
      krypterad = storaalfabetet[bokstav]
      hej += krypterad
    elif character.islower():
      bokstav = (alfabetet.index(character)  +nyckel ) % 28
      krypterad = alfabetet[bokstav]
      hej += krypterad
      
    else:
      hej += character #else här är för ifall användaren skriver ett längre medellande som använder mellan rum som till exempel "Hej hur mår du?" som då använder mellanrum
  return hej

#Jag gör en def main där jag har mina inputs för användaren som sedan kallas i def kryptering.

def main():
  user_input = input("kryptera / dekryptera:")
  nyckel = input("Nyckel:")
  meddelande = input("Skriv ditt meddelande:")

  #Sedan min if sats är ifall användaren väljer att inte skriva in en nyckel så ger den en slumpmässig nyckel.
  if nyckel.isdigit():
    nyckel = int(nyckel)
    printed_nyckel = nyckel     #Jag kom på vad printed_nyckel gör den sparar nyckels originalvärde för print, annars blir den negativ för dekryptering
  else:
    nyckel = random.randint(1,28)
    printed_nyckel = nyckel
  #Här är det för att kryptera eller dekryptera meddelandet då vi använder oss av vad vi fick ifrån user_input och om användaren skriver kryptera eller dekryptera så körs den i följande if sats.
  if user_input == "kryptera":
    krypterad_meddelande = kryptering(nyckel, meddelande)
    print(krypterad_meddelande, printed_nyckel)
  elif user_input == "dekryptera":
    dekrypterad_meddelande = kryptering(-nyckel, meddelande)
    print(dekrypterad_meddelande, printed_nyckel)


main()