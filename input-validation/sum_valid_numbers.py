check = False
total = 0
value = 0
while not check:
    try:
        value = float(input("Enter a number, or 2 non-numbers to quit: "))
        total += value
        
    except ValueError:
        try:
            value = float(input("Enter a number, or another non-number to quit: "))
            total += value
        except ValueError: check = True 
        
print("The total is", total)
