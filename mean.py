def main():
    print(mean([3,7,8,5,12,90,4]))
    
def mean(numbers: list[float]) -> float:
    total = 0
    for x in numbers:
        total += x
    if len(numbers) == 0:
        return 0
    else:
        return total/len(numbers)

if __name__ == "__main__":
    main()