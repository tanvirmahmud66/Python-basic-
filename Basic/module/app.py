import utils
from utils import greater_number

print("Enter 5 Integer Number: ")
numbers = []
for i in range(5):
    numbers.append(int(input()))

maximum = utils.find_max(numbers)
print(f"The maximum value is: {maximum}")

greater_number(40, 28)
