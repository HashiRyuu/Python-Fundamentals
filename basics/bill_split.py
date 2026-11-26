TOTAL_PEOPLE = 4
TIP = 0.15
BILL = 200.0

print("The bill is $", BILL)
print("The tip is $", BILL * TIP)

eachBill = BILL // TOTAL_PEOPLE
eachToTip = eachBill * TIP
print("Each person has to pay $", eachBill + eachToTip)
