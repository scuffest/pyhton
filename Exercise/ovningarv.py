class Bil:
    def __init__(self, marke, modell, ar, hastighet):
        self.marke = marke
        self.modell = modell
        self.ar = ar
        self.hastighet = hastighet

    def starta(self):
        print(f"{self.marke} {self.modell} från {self.ar} har startas")
    
    def stanna(self):
        print(f"{self.marke} {self.modell} från {self.ar} har stannats")
    
    def speed(self):
        print(f"{self.marke} {self.modell} har hastigeten {self.hastighet} i km/h")

    def accelerera(self, okning):
        self.hastighet += okning
        print(f"{self.marke} {self.modell} har accelerats till hastigheten {self.hastighet} i km/h")

    def bromsa(self, minskning):
        self.hastighet -= minskning
        print(f"{self.marke} {self.modell} har bromsat till hastigheten {self.hastighet} i km/h")

class Elbil(Bil):
    def __init__(self, marke, modell, ar, hastighet, batterikapacitet):
        super().__init__(marke, modell, ar, hastighet)
        self.batterikapacitet = batterikapacitet

    def ladda(self):
        print(f"{self.marke} {self.modell} laddas med {self.batterikapacitet} kwh")
              
class Sportbil(Bil):
    def __init__(self, marke, modell, ar, hastighet, turbo):
        super().__init__(marke, modell, ar, hastighet)
        self.turbo = turbo
    
    def aktivera_turbo(self):
        if self.turbo > 0: 
            self.hastighet += 50
            print(f"{self.marke} {self.modell} har aktiverat turbo, {self.hastighet} km/h")
        else:
            print(f"{self.marke} {self.modell} har inte aktiverat turbo, {self.hastighet} km/h")

tesla = Elbil ("Tesla", "Model S", 2021, 100, 60)
ferrari = Sportbil ("Ferrari", "448", 2022, 100, 1)

tesla.starta()
tesla.speed()
tesla.accelerera(60)
tesla.ladda()
tesla.bromsa(30)
tesla.stanna()

ferrari.starta()
ferrari.speed()
ferrari.accelerera(100)
ferrari.aktivera_turbo()
ferrari.bromsa(120)
ferrari.stanna()