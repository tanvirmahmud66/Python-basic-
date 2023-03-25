class Point:  # defining a class called Point. Class name first latter should be in upper case
    def move(self):
        print("Moving")

    def draw(self):
        print("Drawing")

    def calculation(self):
        return 5 + 5


object1 = Point()  # creating object of Point class
object1.move()  # calling class methods
object1.draw()
result = object1.calculation()
print(result)


object2 = Point()
object2.x = 20  # object attribute
object2.y = 30  # object attribute
print(object2.x)
print(object2.y)
