with open("adventcode2.txt", "r") as file:
  all_lines =file.readlines()
  counter = 0
  for rad in all_lines:
    rad = rad.split()
    rad.pop(0)
    game_number = rad[0].strip(":")
    print(game_number)

    rad.pop(0)
    toggle = True
    for index, i in enumerate(rad):
      i.strip(";")
      i.strip(":")
      farg = ""
      if i.isdigit():
        antal = i
      else:
        farg = i
      if int(antal) >12 and farg == "red":
        toggle = False
        print(rad)
    if toggle == True:
      counter += int(game_number)
      
print(counter)