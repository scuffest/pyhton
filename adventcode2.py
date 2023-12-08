with open("adventcode2.txt", "r") as file:
  all_lines =file.readlines()
  for rad in all_lines:
    rad = rad.split()
    rad.pop(0)
    game_number = rad[0].strip(":")
    print(game_number)
    rad.pop(0)
    for index, i in enumerate(rad):
      i.strip(";")
      i.strip(":")
      farg = ""
      if i.isdigit():
        antal = i
      else:
        farg = i
      if int(antal) <13 and farg == "red":
        print(antal + farg)