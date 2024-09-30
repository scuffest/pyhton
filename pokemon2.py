class pokemon:
  def __init__(self, namn, level):
    self.namn = namn
    self.level = level
    self.hp = 100

  def beskrivning(self):
    return f"{self.namn} Level: {self.level} Hp: {self.hp}"


class EldPokemon(pokemon):
  def __init__(self, namn, level):
    super().__init__(namn, level)

  def Eldkast(self):
    return f"{self.namn} använder Eldkast och orsakar 75 skada!"

class VattenPokemon(pokemon):
  def __init__(self, namn, level):
    super().__init__(namn, level)

  def vattenkanon(self):
    return f"{self.namn} använder vattenkanon och orsakar 60 skada!"

class GrasPokemon(pokemon):
  def __init__(self, namn, level):
    super().__init__(namn, level)

  def bladstorm(self):
    return f"{self.namn} använder bladstorm och orsakar 50 skada!"


charmander = EldPokemon("Charmander", 5)
squirtle = VattenPokemon("Squirtle", 5)
bulbasaur = GrasPokemon("Bulbasaur", 5)

print(charmander.beskrivning())
print(charmander.Eldkast())

print(squirtle.beskrivning())
print(squirtle.vattenkanon())

print(bulbasaur.beskrivning())
print(bulbasaur.bladstorm())