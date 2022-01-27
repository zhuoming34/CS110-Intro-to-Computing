# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio

x = random.randint(1, 6)
y = random.randint(1, 6)
z = random.randint(1, 6)

s = x + y + z

print(s)
