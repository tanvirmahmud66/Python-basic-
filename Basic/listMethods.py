numbers = [2, 5, 6, 1, 8, 9, 8]

numbers.append(10)  # will add 10 in the last position in the list
print(numbers)

numbers.insert(0, 20)  # will add 20 in the 0 index or the first position in the list
print(numbers)

numbers.insert(3, 50)  # will add 50 in 3 index
print(numbers)

numbers.remove(1)  # will remove 1 from the list
print(numbers)

# numbers.clear()  # will remove all the item from the list
# print(numbers)

numbers.pop()  # will remove the last item from the list
print(numbers)

print(numbers.index(50))  # will return the index number of 50

print(100 in numbers)  # will return boolean value that the number belongs to the list or not

print(numbers.count(8))  # will return how many times the number 8 have in the list

numbers.sort()  # will sort the list in ascending order by default
print(numbers)

numbers.reverse()  # will sort the list in descending order ( you must have to sort the list before the reverse)
print(numbers)

