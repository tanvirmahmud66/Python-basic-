"""
we can't append or change the item of tuples
we just get information about index number and count method to count the repeated number
we can't change any value of any index
"""

tuples = (1, 3, 5, 8, 3)
print(tuples[1])  # will return the value of index 1 which is 3
print(tuples.count(3))  # will return 2 that number 3 is repeated 2 times in this tuples
