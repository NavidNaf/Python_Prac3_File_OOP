class Vehicle():
    def __init__(self, name, manufacturer, color):
        self.name = name
        self.color = color
        self.manufacturer = manufacturer

    def drive(self):
        print(f"Driving {self.manufacturer} {self.name}")

    def turn(self, direction):
        print(f"Turning {self.name} to {direction}")

    def brake(self):
        print(f"{self.name} is stopping.")


class Car(Vehicle):

    def changeGear(self, gearname):
        print(f"{self.name} is changing gear to {gearname}")


if __name__ == "__main__":
    v1 = Vehicle("Fusion 110X", "Walton", "Black")
    v2 = Vehicle("Softail Deluxe", "Harley-Davidson", "Blue")
    v3 = Vehicle("Mustang 50 GT Coupe", "Ford", "Red")

    v1.drive()
    v2.drive()
    v3.drive()

    v1.turn("Left")
    v2.turn("Right")

    v1.brake()
    v2.brake()
    v3.brake()
