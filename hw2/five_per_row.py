# five_per_row.py: writes the integers 101 to 200 with five numbers per line.

import stdio
import sys

# Iterate over the integers 101 to 200, and write five of them per row.
for num in range(101, 201, 5):
    # If the integer is a multiple of 5, write the integer followed by a
    # new line. Otherwise, write the integer followed by a space.
    if (num % 5 == 0):
        stdio.writeln('\n')
    else:
        stdio.writeln(str(num) + ' ' + str(num+1) + ' ' + str(num+2) +
                      ' ' + str(num+3) + ' ' + str(num+4))
