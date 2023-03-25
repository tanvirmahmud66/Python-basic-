def find_max(numbers):
    maximum = numbers[0]
    for each in numbers:
        if each > maximum:
            maximum = each
    return maximum


def greater_number(value1, value2):
    if value1 > value2:
        print(f"The large value is : {value1}")
    else:
        print(f"The large value is: {value2}")
