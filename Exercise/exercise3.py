import random

#Del 1
#Uppgift 1
def varld():
  print("Hej värdlen!")
varld() 

#Uppgift 2
def sol():
  print("*")
sol()

#Uppgift 3
def emoji():
  print(":)")
emoji()

#Del 2
#Uppgift 1

namn = input("Skriv ditt namn:")

def namnet():
  print("Hej", namn)

namnet()

#Uppgift 2

number = [1,2,3,4,5]

def numbers(number):
  print("Alla element är", len(number))
numbers(number)
#Uppgift 3
a = int(input("Skriv ett heltal"))
b =int(input("Skriv ett till heltal:"))

def tal(a , b):
  if a > b:
    print(a, "är större än", b)
  elif b>a:
    print(b, "Är större än", a)
  else:
    print(a, "är lika med", b)

tal(a, b)
#Uppgift 4

c = int(input())

def gangertabell(c):
  print("Gånger tabellen är:", c*1, c*2, c*3, c*4, c*5, c*6, c*7, c*8, c*9, c*10)
gangertabell(c)