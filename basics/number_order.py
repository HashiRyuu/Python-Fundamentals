n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

if n1 < n2 < n3:
    print("They are in increasing order.")
elif n1 > n2 > n3:
    print("They are in decreasing order.")
else :
    print("They are neither in increasing order nor decreasing order.")
