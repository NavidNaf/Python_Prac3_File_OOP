class Car:
    name = ""
    color = ""

    def start():
        print("Starting the Engine")


Car.name = "Toyota"
Car.color = "Yellow"

print(Car.name)
print(Car.color)
Car.start()
print(dir(Car))
