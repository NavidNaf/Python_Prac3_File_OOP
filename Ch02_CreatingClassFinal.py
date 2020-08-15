class raceCar():
    def __init__(self, n, m, c, y, cc):
        self.name = n
        self.manufact = m
        self.color = c
        self.year = y
        self.cc = cc

    def start(self):
        print(self.name, self.manufact, self.color, self.year, self.cc)
        print("Engine is Starting")

    def brake(self):
        print("Engine is Braking")

    def drive(self):
        print("We are in motion.")

    def turn(self, t):
        if t == "L":
            print("Turning Left")
        elif t == "R":
            print("Turning Right")

    def changeGear(self):
        print("Changing Gear")


newCar1 = raceCar("Toyota", "Toyota", "Blue", 2017, 1500)
newCar2 = raceCar("Veyron", "Bugatti", "Yellow", 2011, 2500)
newCar3 = raceCar("Pagani Zonda", "Pagani", "Red", 2009, 2500)

newCar1.start()
newCar1.brake()
newCar1.drive()
newCar1.turn("L")
newCar1.changeGear()

newCar2.start()
newCar2.brake()
newCar2.drive()
newCar2.turn("R")
newCar2.changeGear()

newCar3.start()
newCar3.brake()
newCar3.drive()
newCar3.turn("L")
newCar3.changeGear()