class car:
    def __init__(self, n, c, m):
        self.name = n
        self.color = c
        self.manufacturer = m

    def start(self):
        print(self.name)
        print(self.color)
        print(self.manufacturer)
        print(self.year)
        print("Starting the Engine.")


myCar = car("Bugatti", "Green", "Volkswagen")
myCar1 = car("Premio", "White", "Toyota")
myCar2 = car("Axio", "Black", "Toyota")
myCar.year = 2017

print(myCar.name, myCar.color, myCar.year)
myCar.start()
myCar1.start()
myCar2.start()

# print(dir(car))
# print(dir(myCar))
# car.start(myCar)
