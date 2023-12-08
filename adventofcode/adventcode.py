with open("adventcode.txt", "r", encoding="utf-8") as file:
    hej = file.readlines()
    counter = 0
    for i in hej:
        my_lista = []
        for z in list(i):
            if z.isdigit():
              my_lista.append(z)
        if len(my_lista) > 0:
          counter += int(str(my_lista[0])+str(my_lista[-1]))

    print(counter)