people = [
    {"name": "Tanvir", "House": "Rajshahi"},
    {"name": "Mominul", "House": "Chapai"},
    {"name": "Anonna", "House": "Dhaka"}
]

# like javascript we can also use arrow funciton in python which is call lambda
def f(person):
    return person["name"]

people.sort(key=f)
print(people)

#lambda
people.sort(key=lambda person: person["House"])
print(people)
