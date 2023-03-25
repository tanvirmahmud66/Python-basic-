class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    def greeting(self):
        print(f"Hi, {self.name}")


p1 = Person("Tanvir")
p1.print_name()
p1.greeting()

p2 = Person("Fahim")
p2.print_name()
p2.greeting()

