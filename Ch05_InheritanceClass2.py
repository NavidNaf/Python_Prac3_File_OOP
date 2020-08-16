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
    c = Car("Supra", "Toyota", "Black")

    c.drive()
    c.turn("Left")
    c.changeGear("D")
    c.brake()
