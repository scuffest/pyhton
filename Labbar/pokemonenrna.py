class Pokemon:
  def __init__(self, name, lvl, type, hp):
    self.name = name
    self.lvl = lvl
    self.type = type
    self.hp = hp
    self.fullhp = hp

  def beskrivning(self):
    print(f"{self.name}, Nivå:{self.lvl}, Typ:{self.type}, HP:{self.hp}")

  def trana(self):
    self.lvl += 1
    print(f"{self.name} Har gått upp med 1 nivå")

  def utvecklas(self, nytt_namn):
    print(f"{self.name} har elvoverat till {nytt_namn}")
    self.name = nytt_namn
  
  def attackera(self, motstandare):
    motstandare.hp -= self.lvl
    print(f"{self.name} attackerar {motstandare.name} för {self.lvl}")

  def laka(self):
    self.hp = self.fullhp
    print(f"{self.name} har läkts till {self.fullhp}")

  def ar_levande(self):
    if self.hp > 0:
      print(f"{self.name} lever fortfarande")
    elif self.hp == 0:
      print(f"{self.name} är död")
    else:
      print(f"{self.name} är levande")


    
pikachu = Pokemon("Pikachu", 5, "Elektrisitet", 100)
bulbasaur = Pokemon("Bulbasaur", 5, "Gräs", 100)

pikachu.beskrivning()
bulbasaur.beskrivning()

pikachu.trana()
pikachu.beskrivning()

bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
bulbasaur.attackera(pikachu)
pikachu.ar_levande()
pikachu.beskrivning()

pikachu.laka()
pikachu.beskrivning()

pikachu.utvecklas("Raichu")
pikachu.beskrivning()