import turtle


class DrunkTurtle(turtle.Turtle):
    def forward(self, pixel):
        super().backward(pixel)

    def backward(self, pixel):
        super().forward(pixel)

    def left(self, angle):
        super().right(angle)

    def right(self, angle):
        print("I won't Turn Right, Man!")


alvin = DrunkTurtle()

alvin.shape("turtle")
alvin.left(30)
alvin.forward(200)
alvin.left(45)
alvin.backward(100)
alvin.right(90)
alvin.forward(10)

christopher = turtle.Turtle()
christopher.left(30)
christopher.forward(200)
christopher.left(45)
christopher.backward(100)
christopher.right(90)
christopher.forward(10)
