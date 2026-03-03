stringgg = str(input("Enter the palindrome: "))

stringgg = stringgg.replace(" ", "")

stringggLen = len(stringgg)

isPalindrome = True

if stringgg != "":
    for x in range(0, stringggLen//2):
        if stringgg[x].upper() != stringgg[stringggLen-x-1].upper():
            isPalindrome = False
            break
    if isPalindrome:
        print("This is Palindrome!")
    else:
        print("This isn't a Palindrome!")
else:
    print(f"Enter something dude!")



