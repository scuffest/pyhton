import random
from cmath import pi
#Del 1
#Uppgift 1



def random_nummer():
  number = random.randint (1, 100)
  return number
u = random_nummer()
print(u)

#Uppgift 2

halsning = ["Hej", "Hejsan", "God dag", "Hallå", "God natt"]

def generate_greeting():
  return random.choice(halsning)
halsning = generate_greeting()
print(halsning)

#Del 2
#Uppgift 3

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum_element(number):
  summ = sum(number)
  return summ


summ= sum_element(number)
print(summ)
#Uppgift 4

r=int(input("Skriv in ett heltal:"))

def area(r):
  o = 2*pi*r
  a = pi*r*r
  return a, o

o, a = area(r)
print("Arean är:", a, "Omkretsen är:", o)


#Uppgift 5

def funktion(k, l):
  donut = k + " " + l
  return donut
c = funktion("Hej", "Hejsan")
print(c)



 