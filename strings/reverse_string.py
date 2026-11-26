string = input("Enter a word: ")
length = len(string)

reverse = ""
for i in range(length - 1, -1, -1):
    reverse += string[i]

print(f"{string} reversed is {reverse}")
