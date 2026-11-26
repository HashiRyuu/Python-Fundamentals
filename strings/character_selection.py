string = input("Enter a string: ")
length =  len(string)

remove = ""
replace = ""

i = 0
while i < length:
    if string[i] in "aeiouAEIOU":
        replace += "_"
    else:
        replace += string[i]
        
    if i % 2 == 0:
        remove += string[i]
        
    i += 1
    
print("The string with every second letter printed is: ", remove)
print("The string with every vowel replaced with  -  is: ", replace)
