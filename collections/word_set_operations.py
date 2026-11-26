string1 = set(input("Enter the first string: ").split())
string2 = set(input("Enter the second string: ").split())

sameWord = sorted(string1.intersection(string2))
diff1 = sorted(string1.difference(string2))
diff2 = sorted(string2.difference(string1))

print("The words that are in both strings:")
for value in sameWord:
    print(value.lower(), end=" ")


print("\nThe words in string 1 that are not in string 2:")
for value in diff1:
    print(value.lower(), end=" ")


print("\nThe words in string 2 that are not in string 1:")
for value in diff2:
    print(value.lower(), end=" ")
