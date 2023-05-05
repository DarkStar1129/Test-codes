# Coin flip program with multiple flips

import random

# Define the two possible outcomes
outcomes = ['Heads', 'Tails']

# Prompt user for number of flips
num_flips = int(input('How many times do you want to flip the coin? '))

# Simulate the coin flips and count the number of times each outcome occurs
heads_count = 0
tails_count = 0

for i in range(num_flips):
    result = random.choice(outcomes)
    if result == 'Heads':
        heads_count += 1
    else:
        tails_count += 1

# Print the results of the coin flips
print('Number of Heads:', heads_count)
print('Number of Tails:', tails_count)