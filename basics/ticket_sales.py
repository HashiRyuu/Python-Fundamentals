print("There are currently 40 tickets remaining.")

count = 0
tickets = 40
while tickets > 0:
    purchase = int(input("How many tickets would you like to purchase? "))
    
    if purchase > 0 and purchase <= 10 and purchase <= tickets:
        tickets -= purchase
        count += 1
        if tickets != 0:
            print(f"There are currently {tickets} tickets remaining.")        
    else:
        print("Sorry, you can't buy that many.")    
    
print("The total number of buyers was", count)
