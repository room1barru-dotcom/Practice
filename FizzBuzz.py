def main():
    for n in range(1,101):
        if n%3 == 0 and n%5 == 0:  # Specific first
            print("3 and 5 both are divisable!")
        elif n%3 == 0:             # General Later
            print("Divisable by 3!")
        elif n%5 == 0:
            print("Divisable by 5!")
        else:
            print(n)

if __name__ == "__main__":
    main()