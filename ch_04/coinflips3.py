import random
from random import choices
from statistics import mean

NUM_EXPERIMENTS = 10_000

experiments_with_streak = 0

for _ in range(NUM_EXPERIMENTS):
    streak = 0
    for _ in range(99):
        same = random.choice((True, False))
        streak = streak + 1 if same else 0
        if streak == 5:
            experiments_with_streak += 1
            break

print('Chance of streak: %.2f%%' % (100 * experiments_with_streak / NUM_EXPERIMENTS))


chance = mean('s' * 5 in ''.join(choices('sd', k=99))
              for _ in range(10000))

print('Chance of streak: %.2f%%' % (100 * chance))