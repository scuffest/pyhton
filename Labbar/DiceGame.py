import random

def kasta_tarning():
  return random.randint(1, 6)

def spelaren_kast():
  counter = 0
  while True:
    svar = input("Vill du forsätta kasta?")
    if svar == "ja":
      k = kasta_tarning()
      print("Du fick:", k)
      counter += k
      print("Du har totalt:", counter)
    elif svar =="nej":
      break
  return counter

def dealerns_kast():
  w = 0
  while w <= 17:
      j = kasta_tarning()
      print("Dealern fick:", j)  
      w += j
      print("Dealern har totalt:", w)
  return w

def avgora_vinnare(spelare_poang, dealer_poang):
  if spelare_poang > dealer_poang:
    print("Du vann!")
  elif dealer_poang > spelare_poang:
    print("Dealern vinner!")
  else:
    print("Det blev oavgjord")

def spela_igen():
  while True:
    svaret = input("Vill du spela igen?")
    if svaret == "ja":
      main()
    else:
      print("Hejdå!")
      exit()

def main():
  spelare_poang=spelaren_kast()
  dealer_poang=dealerns_kast()
  avgora_vinnare(spelare_poang, dealer_poang)
  spela_igen()
  
main()

  


