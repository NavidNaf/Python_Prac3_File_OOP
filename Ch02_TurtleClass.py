import turtle

jerry = turtle.Turtle()
tom = turtle.Turtle()
spike = turtle.Turtle()

jerry.speed(2)
jerry.shape("square")

tom.speed(2)
tom.shape("circle")

spike.speed(2)
spike.shape("turtle")
spike.setpos(-100, -100)

jerry.forward(200)
jerry.left(35)
tom.forward(95)
spike.forward(50)
spike.left(45)
spike.forward(200)
jerry.forward(120)
tom.right(45)
tom.forward(100)


tom.clear()
jerry.clear()
spike.clear()
turtle.done()
