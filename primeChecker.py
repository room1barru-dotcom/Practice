def main():
    num = int(input("Enter the number to check if it is prime: "))

    totalDivided = 0

    for x in range(1, num+1):
        print("Loop executed!")
        if num%x == 0:
            totalDivided +=1
            print("Divisable!")

    if(totalDivided == 2):
        print(f"This is a prime number!")
    else:
        print(f"This isn't a prime number!")

if __name__ == "__main__":
    main()