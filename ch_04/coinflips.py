import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = []
    for flip in range(100):
        flips.append(random.randint(0,1))
    
    # Code that checks if there is a streak of 6 heads or tails in a row.

    for i in range(len(flips)):
        if i == 0:
            streak = 1
            # initialize variable
        elif flips[i] == flips[i-1]:
            streak += 1
        else:
            streak = 1
            # initialize variable again
        
        if streak == 6:
            # either initialize streak = 0 and count till 5
            # or initialize streak = 1and count till 6
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
# numberOfStreaks / 10000 (number of experiments) * 100 (for %) = numberOfStreaks / 100
# using a variable like `experiments` would have made it easier to understand 
# number of experiments with a streak divided by the number of experiments times 100 -> %