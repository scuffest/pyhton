def medeltemp():
    with open("Labbar/temperaturdata.txt", "r", encoding="utf-8") as file:
        file.readline()
        for i in file:
          lista = i.strip().split(",")
          stad = lista.pop(0)
          medel = []
          for a in lista:
             medel.append(int(a))
          medelvarde = sum(medel) / len(lista)
          print(stad, medelvarde)
          high = max(medel)
          low = min(medel)
          print(f"I {stad} så var den högsta temperaturen {high} och minsta {low}")
medeltemp()

