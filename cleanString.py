def main():
    
    print(cleanString(str(input("Enter something: "))))
    
def cleanString(s: str) -> str:
        return s.strip().lower()

if __name__ == "__main__":
    main()