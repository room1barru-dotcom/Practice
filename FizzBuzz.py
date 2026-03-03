
for n in range(1,101):
    if n%3 == 0 and n%5 == 0:
        print("3 and 5 both are divisable!")
    elif n%3 == 0:
        print("Divisable by 3!")
    elif n%5 == 0:
        print("Divisable by 5!")
    else:
        print(n)

# i need to check the rare conditions first so the if,elif block dont exit when general condition gets true.
# means, high speed train is also a train, if i check if this is a train? but that is a high speed train
# the if will say "Yes, this is a train" and we exit out without knowing if it is a high speed train?
# so structuring the if,elif block to check the rare conditions first and general conditions later.
# Most Specific -> General
