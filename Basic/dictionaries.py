customer = {
    "name": "Tanvir Mahmud",
    "age": 26,
    "student": True,
    "job": False,
    "birthday": "5th March 1998"
}

print(customer)
print(customer["name"])
print(customer["age"])
print(customer["student"])

print(customer.get("Name"))
print(customer.get("name"))

# update a value
customer["name"] = "Tanvir Mahmud Fahim"
print(customer.get("name"))

# add a new value
customer["mail"] = "tanvirmahmudfahim1313@gmail.com"
print(customer)