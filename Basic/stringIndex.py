department = "Computer Science and Engineering"

# print index from start
print(department[0])  # will print C
print(department[1])  # will print o
print(department[2])  # will print m

# print index from last
print(department[-1])  # will print g
print(department[-2])  # will print n
print(department[-3])  # will print i


# print character with range
print(department[0:5])  # will print Compu
print(department[:5])  # here start index assume 0 and will print Compu
print(department[1:5])  # will print ompu
print(department[0:-1])  # will print all the character except last character
print(department[1:])  # will print all the character from second index
print(department[:])  # will print all the character

subject = department[:]  # will copy all the character from department to subject

