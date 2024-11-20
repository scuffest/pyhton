class Vehicle:
  def __init__(self, brand, model, year, speed, fuel, maxfuel):
    self.__brand = brand
    self.__model = model
    self.__year = year
    self.__speed = speed
    self.__fuel = fuel
    self.__maxfuel = maxfuel
  
  def start(self):
    if self.__fuel > 0:
      print(f"{self.__brand} {self.__model} från {self.__year} har startats. Bensinnivån från {self.__maxfuel} minskar till {self.__fuel} liter")
    else:
      print(f"{self.__brand} {self.__model} har inte tillräckligt med bränsle för att starta.")

    # Brake method with adjustable speed decrease
  def brake(self, minskning):
    self.__speed -= minskning
    if self.__speed < 0:
      self.__speed = 0  # Se till att hastigheten inte blir negativ
      print(f"{self.__brand} {self.__model} har bromsat till hastigheten {self.__speed} km/h")

    # Refuel method that refuels the vehicle to its max capacity
  def refuel(self):
        self.__fuel = self.__maxfuel
        print(f"{self.__brand} {self.__model} har tankats till {self.__maxfuel} liter")

    # Getter methods
  def get_brand(self):
    return self.__brand

  def get_model(self):
        return self.__model

  def get_year(self):
        return self.__year

  def get_speed(self):
        return self.__speed

  def get_fuel(self):
        return self.__fuel

    # Setter methods
  def set_speed(self, new_speed):
        self.__speed = new_speed

  def set_fuel(self, new_fuel):
    self.__fuel = new_fuel


# Subklasser
class Car(Vehicle):
  def __init__(self, brand, model, year, speed, fuel):
    # Använd maxfuel = 150 för bilar
    super().__init__(brand, model, year, speed, fuel, 150)

    # Accelerate method specific to Car (utan super)
  def accelerate(self):
    self.set_speed(self.get_speed() + 10)  # Öka hastigheten med 10
    self.set_fuel(self.get_fuel() - 5)     # Minska bränslet med 5 liter
    print(f"{self.get_brand()} {self.get_model()} har accelererat till hastigheten {self.get_speed()} km/h. Bensinnivån minskar till {self.get_fuel()} liter")

  def honk(self):
    print(f"{self.get_brand()} {self.get_model()} tutar BEEP!")


class Truck(Vehicle):
  def __init__(self, brand, model, year, speed, fuel):
   # Använd maxfuel = 200 för lastbilar
   super().__init__(brand, model, year, speed, fuel, 200)

    # Accelerate method specific to Truck (utan super)
  def accelerate(self):
    self.set_speed(self.get_speed() + 20)  # Öka hastigheten med 20
    self.set_fuel(self.get_fuel() - 10)    # Minska bränslet med 10 liter
    print(f"{self.get_brand()} {self.get_model()} har accelererat till hastigheten {self.get_speed()} km/h. Bensinnivån minskar till {self.get_fuel()} liter")

  def honk(self):
    print(f"{self.get_brand()} {self.get_model()} tutar MÖÖÖÖÖ!")


class Motorcycle(Vehicle):
  def __init__(self, brand, model, year, speed, fuel):
    # Använd maxfuel = 50 för motorcyklar
    super().__init__(brand, model, year, speed, fuel, 50)

    # Accelerate method specific to Motorcycle (utan super)
  def accelerate(self):
    self.set_speed(self.get_speed() + 5)  # Öka hastigheten med 5
    self.set_fuel(self.get_fuel() - 3)    # Minska bränslet med 3 liter
    print(f"{self.get_brand()} {self.get_model()} har accelererat till hastigheten {self.get_speed()} km/h. Bensinnivån minskar till {self.get_fuel()} liter")

  def honk(self):
    print(f"{self.get_brand()} {self.get_model()} tutar Vroom Vroom!")


car = Car("Toyota", "Corolla", 2020, 100, 50)
truck = Truck("Volvo", "FH16", 2018, 80, 150)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021, 60, 30)

car.start()
car.accelerate()
car.brake(60)
car.refuel()

motorcycle.start()
motorcycle.accelerate()
motorcycle.brake(20)
motorcycle.refuel()

truck.start()
truck.accelerate()
truck.brake(30)
truck.refuel()

car.honk()
motorcycle.honk()
truck.honk()