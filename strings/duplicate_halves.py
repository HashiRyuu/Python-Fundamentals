string = input("Enter a string: ")
length = len(string)
middle = length // 2

firstHalf = string[0:middle] * 2
secondHalf = string[middle:] * 2

print(firstHalf + secondHalf)
