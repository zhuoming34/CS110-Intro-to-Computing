# order_check.py: Takes three floats values x, y, and z as command-line
# arguments and prints True if the values are strictly ascending or
# descending (i.e., x<y<z or x>y>z), and False otherwise.

import stdio
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if (x < y) and (y < z):
    print('True')
elif (x > y) and (y > z):
    print('True')
else:
    print('False')
