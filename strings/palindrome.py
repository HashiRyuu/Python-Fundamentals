def isPalindrome(string):
    for i in range(len(string)):
        if string[i] == string[len(string) - 1 - i]:
            return True
    return False

def main():
    string = input("Enter a string: ")
    if isPalindrome(string):
        print("That's a palindrome.")
    else:
        print("That isn't a palindrome.")

main()
