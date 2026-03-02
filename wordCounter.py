def main():
    sentance = input("Enter your sentance: ") # string from the user

    words = sentance.split() # returns a list of words

    count = len(words) # Counts the elements

    print(f"Total words in the snetance is : {count}") # Prints the words

if __name__ == "__main__":
    main()