def main():

    if emailValidate(input("Enter your email: ")):
        print("Valid!")
    else:
        print("Invalid!")

def emailValidate(email: str) -> bool:

    if len(email) > 5:
        adroid_i = email.find("@")
        atCount = email.count("@")
        if atCount == 1:
            dot_i = email.find(".", adroid_i)
            return dot_i != -1 and adroid_i > 0 and dot_i != len(email)-1
        else:
            return False
    
    else:
        return False
    
if __name__ == "__main__":
    main()