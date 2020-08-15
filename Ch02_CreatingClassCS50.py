class student():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def changeID(self, id):
        self.id = id

    def printStudent(self):
        print(f"{self.name} - {self.id}")


Jane = student("Jane", 57)
Jane.changeID(55)
Jane.printStudent()

Kyle = student("Kyle", 88)
Kyle.printStudent()

Naf = student("Naf", 33)
Naf.changeID(16)
Naf.changeID(28)
Naf.printStudent()
