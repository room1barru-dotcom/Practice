states = {"USA":"TEXAS", "INDIA":"MAHARASHTRA", "JAPAN":"TEXAS"}

frequency = {}

for x in states:
    if states[x] in frequency:
        frequency[states[x]] += 1
    else:
        frequency[states[x]] = 1

print(frequency)