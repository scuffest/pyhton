import random

user_input = input("kryptera / dekryptera:")
nyckel = input("Nyckel:")
meddelande = input("Skriv ditt meddelande:")

if nyckel.isdigit():
  nyckel = int(nyckel)
  printed_nyckel = nyckel

else:
  nyckel = random.randint(1,28)
  printed_nyckel = nyckel


def kryptering(nyckel, meddelande):
  alfabetet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
  storaalfabetet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Å", "Ä", "Ö"]
  hej = ""

  for character in meddelande:
    if character.isupper():
      bokstav =   (storaalfabetet.index(character)  +nyckel)   % 28
      krypterad = storaalfabetet[bokstav]
      hej += krypterad
    elif character.islower():
      bokstav = (alfabetet.index(character)+nyckel) %28
      krypterad = alfabetet[bokstav]
      hej += krypterad
    else:
      hej += character
  print(hej, printed_nyckel)

if user_input == "kryptera":
  kryptering(nyckel, meddelande)
elif user_input == "dekryptera":
  kryptering(-nyckel, meddelande)