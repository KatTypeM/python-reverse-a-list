# python algorithm

# reverse a list (array) using an algorithm

numbers = [12, 23, 100, 53, 34, 76, 86,99, 43, 67, 9,1,56,190,567, -24]
numbersReverse = []

# find length of list
for i in range(0, len(numbers)):
    # create temp number to count back
    listLocation = len(numbers) - 1 - i
    # append new list (array) with number counting backwards
    numbersReverse.append(numbers[listLocation])
    continue

print(numbers)
print(numbersReverse)
