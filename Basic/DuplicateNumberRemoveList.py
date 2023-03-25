numbers = [2, 2, 5, 1, 5, 8, 9, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
