phone = input("Enter your phone number: ")
number_book = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

output = ""
for each in phone:
    output += number_book.get(each) + " "

print(output)
