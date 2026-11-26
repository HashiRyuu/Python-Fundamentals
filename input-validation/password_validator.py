def isValidPassword(string):
    
    reEnter = input("Re-Enter your password: ")
    
    if reEnter != string:
        print("That passwords don't match")
        return False
    
    elif len(reEnter) < 8:
        print("That password didn't have the required properties.")
        return False
    
    else:
        state1 = False
        state2 = False
        state3 = False
        state4 = False
        for ch in reEnter:
            
            if ch.islower():
                state4 = True
            if ch.isupper():
                state1 = True
            if ch.isdigit():
                state2 = True
            if ch in "#@&":
                state3 = True
                
            if state1 and state2 and state3 and state4: 
                print("That pair of passwords will work.")                
                return True
         
        print("That password didn't have the required properties.")
        return False
            
        
def main():
    
    check = False
    while not check:
        password = input("Enter your password: ")
        check = isValidPassword(password)     


main()
