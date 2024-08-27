import random

def temperaturenarbra():
  
  temp = int(input("Skriv vad temperaturen är:"))

  if temp > 18:
    print("Det är varmt")
  elif temp == 18:
    print("det är rums temperatur")
  elif temp < 18:
    print("det är kallt")
temperaturenarbra()

def tal():
  tal = int(input("Skriv ett tal: "))
  if tal % 2 == 0:
    print("talet är jämt")
  else:
    print("talet är udda")
tal()

def jagvillinte():
  hej = input("Skriv a för addition s för subtration d division m multiplikation")
  nej = int(input("Välj ett nummer"))
  okej = int(input("Välj ett till nummer"))
  if hej == "a":
    print(nej + okej)
  elif hej == "s":
    print(nej - okej)
  elif hej == "d":
    print(nej / okej)
  elif hej == "m":
    print(nej*okej)
jagvillinte()



def loopar():
  for i in range(1, 11):
    if  i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")

    elif i % 5 == 0:
      print("Buzz")

    elif i % 3 == 0:
      print("Fizz")

    else:
      print(i)

def summera():
  k = int(input("Skriv ett tal:"))
  x = 0
  for i in range(1, k+1):
    if i % 2 == 0:
      x += i
  print(x)

def uppgift6():
  w = random.randint(1, 20)
  while True:
    q = int(input("Skriv in ett slumpmässigt tal:"))
    if w == q:
      print("Du gissade rätt!")
      break
    elif w > q:
      print("Talet är större.")
    else:
      print("Talet är mindre.")

uppgift6()