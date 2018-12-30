class Person:
    def __init__(self, p1):
        self.name = p1
        self.country = "India"

    def display(self):
        print("I am " + self.name + " From " + self.country)


p2 = Person("Adarsh")

p2.display()
