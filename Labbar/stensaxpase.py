import random
def ssp():
  t = input("Sten/sax/påse:")
  y = ["sten", "sax", "påse"]
  k = random.choice(y)
  if t==k:
    print("Det blev oavgjort!")
  elif t=="sax" and k=="påse" or t=="påse" and k=="sax" or t=="sten" and k=="påse" 

ssp()
