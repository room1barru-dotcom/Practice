num = [-20, -5, -1, -10]

min = num[0]
max = num[0]

for x in num:
    # This is for finding minimum
    if x < min:
        min = x
    # This is for finding maximum
    if x > max:
        max = x

print(f"Minimum is {min}, Max is {max}")
