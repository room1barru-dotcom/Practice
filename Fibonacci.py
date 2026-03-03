num = int(input("Enter how many fibonacci you want: "))

previous = 0
current = 1

for x in range(0, num):
    print(f"{previous}")
    next = previous + current
    previous = current
    current = next