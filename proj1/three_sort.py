# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

num1 = min(x, y, z)
num3 = max(x, y, z)


if (num1 == x):
    if (num3 == z):
        num2 = y
    else:
        num2 = z
elif (num1 == y):
    if (num3 == z):
        num2 = x
    else:
        num2 = z
else:
    if (num3 == x):
        num2 = y
    else:
        num2 = x

print(num1, num2, num3)
