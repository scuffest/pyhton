stader = ["Stockholm" , "Göteborg" , "Malmö" , "london" , "frankfurt"]
print(stader)
print(stader[2])

stader.append("helsingfors")
print(stader)

stader.remove(stader[1])
print(stader)

numbers = []
for k in range (1,11):
  numbers .append(k)


langd = 5
bredd = 3

def area_rectangle(langd , bredd):
  area = langd * bredd
  return area
area = area_rectangle(langd , bredd)
print(area_rectangle(langd , bredd))


tal = int(input("Skriv ett tal:"))
def is_even(tal):
  if tal % 2 == 0:
    return True
  else:
    return False
resultat = is_even(tal)
print(resultat)

def reverse_list(numbers):
  reversed = numbers[::-1]
  return reversed

reversed_tal = reverse_list(numbers)
print("List reversed:", reversed_tal)