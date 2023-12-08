#Uppgift 1
def multiplikation(a, b):
  return a*b

def division(a, b):
  
  if b == 0:
    return "Kan inte dividera med noll"
  return a/b


def plus(a, b):
  return a+b

def minus(a, b):
  return a-b

print("1. är addition")
print("2. är subtration")
print("3. är multiplikation")
print("4. är division")

a =int(input("ange första talet"))
b =int(input("ange andra talet"))
k=int(input("ange operationen"))

if k == 1:
    print("Resultat:", plus(a, b))
elif k == 2:
    print("Resultat:", minus(a, b))
elif k == 3:
    print("Resultat:", multiplikation(a, b))
elif k == 4:
    print("Resultat:", division(a, b))
else:
   print("Ogiltig operation.")


