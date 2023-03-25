class Animal:
    def walk(self):
        print("walk")

    def run(self):
        print("run")


class Cat(Animal):
    pass


class Dog(Animal):
    def bark(self):
        print("Bark")


c1 = Cat()
c1.walk()
c1.run()

d1 = Dog()
d1.walk()
d1.run()
d1.bark()

