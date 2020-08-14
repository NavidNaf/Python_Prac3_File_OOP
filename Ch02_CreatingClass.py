class Car:
    name = "BMW"
    color = "Blue"

    def start():
        print("The Engine is Starting.")


print(Car.name)
print(Car.color)
Car.name = "Toyota"
Car.color = "Yellow"


print(Car.name)
print(Car.color)
Car.start()
