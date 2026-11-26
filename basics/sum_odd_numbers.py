a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

sum = 0
i = a
while i <= b:
    if i % 2 != 0:
        sum += i
    i += 1
print(f"The sum of odd numbers between {a} and {b} is: {sum}")
