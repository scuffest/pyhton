import random

#Uppgift 1
def uppgift1():
  x = 11

  while x >= 1:
    print(x)
    x -= 1

uppgift1()


#Uppgift 2
def uppgift2():
  nummer = int(input("Skriv ett tal:"))
  iter = 0

  while nummer < 1000:
    print(nummer)
    nummer *= 2
    iter += 1

  print("Iteration:", iter)

uppgift2()

#Uppgift 3
def uppgift3():
  a = int(input("Skriv ett tal:"))
  n = a
  while a != 0:
    a = int(input("Skriv ett tal:"))
    n +=a
  print("Summan är:", n)
uppgift3()

#Uppgift 4
def uppgift4():
  r = 1
  while r <= 10:
    print(r)
    r += 1

uppgift4()

#Uppgift 5
def uppgift5():
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

uppgift5()