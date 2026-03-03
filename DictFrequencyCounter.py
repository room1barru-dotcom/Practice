import listMinMaxFinder

def main():
    states = {"india":"delhi", "USA":"Texas", "JAPAN":"delhi"}

    frequency = {}

    for x in states:
        if states[x] in frequency:
            frequency[states[x]] += 1
        else:
            frequency[states[x]] = 1


    print(frequency)

if __name__ == "__main__":
    main()