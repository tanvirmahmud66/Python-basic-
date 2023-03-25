is_hot = False
is_cold = False

if is_hot:
    print("It is hot day")
    print("Drink Plenty of water")
elif is_cold:
    print("It is cold day")
    print("Wear warm clothes")
else:
    print("It is lovely day")
    print("Enjoy your day")


x = int(input("Enter a number: "))

if x < 100:
    print(f'{x} is less than 100')
elif x > 100:
    print(f'{x} is greater than 100')
elif x == 100:
    print(f'{x} is equal to 100')
