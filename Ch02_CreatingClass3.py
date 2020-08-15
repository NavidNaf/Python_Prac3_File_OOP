class car:
    name = ""
    color = ""

    def start(self):
        print("Starting the Engine.")


myCar = car()

myCar.name = "Pagani Zonda"
myCar.color = "Red and Black"

print(myCar.name)
print(myCar.color)

myCar.start()
