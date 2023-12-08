

numbers = []
for k in range (1,11):
  numbers .append(k)

lista = numbers
def summan_av_element(lista):
  total_sum = sum(lista)
  return total_sum
lista_klass = summan_av_element(lista)
print("Summan är:", lista_klass)

def medelvarde(lista):
  antal_number=len(lista)
  number_sum = sum(lista)
  medelvarde_elever=number_sum / antal_number
  return medelvarde_elever

medelvarde_av_elever=medelvarde(lista)
print("Medelvärdet är:", medelvarde_av_elever)

def max_varde(lista):
  max_nummer=max(lista)
  return max_nummer
max_vardet_lista=max_varde(lista)
print("Maxvärdet är:", max_vardet_lista)

def min_varde(lista):
  min_nummer=min(lista)
  return min_nummer
min_vardet_lista=min_varde(lista)
print("Minsta värdet är:", min_vardet_lista)

