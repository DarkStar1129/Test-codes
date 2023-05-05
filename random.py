# Random number generator

import random

# Prompt user for range of numbers
min_num = int(input('Enter the minimum number: '))
max_num = int(input('Enter the maximum number: '))

# Generate a random number within the specified range
rand_num = random.randint(min_num, max_num)

# Print the random number
print('Your random number is:', rand_num)