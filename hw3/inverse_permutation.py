# inverse_permutation.py: accepts a permutation of the integers 0
# through n-1 as n command-line arguments and writes its inverse.

import stdarray
import stdio
import sys

# Create a list perm consisting of the integers from the command line.
perm = sys.argv[1:]
for v in range(1, len(sys.argv)):
    perm[v-1] = int(perm[v-1])

# Define a variable n and set it to the number of elements in perm.
n = len(perm)

# Make sure perm represents a valid permutation. If not, exit the program
# with the message 'Not a permutation'. Use a 1D list exists of n booleans
# for this purpose; perm is not a permutation if perm[i] < 0 or
# if perm[i] > n - 1 or if exists[perm[i]] is True.
exists = stdarray.create1D(n, bool)
for i in range(n):
    if (perm[i] < 0) or (perm[i] > n-1) or (exists[perm[i]] is True):
        sys.exit("Not a permutation")
    exists[perm[i]] = True

# Invert the permutation into a list perm_inverted, using the definition
# perm_inverted[perm[i]] = i.
perm_inverted = stdarray.create1D(n, 0)
for i in range(n):
    perm_inverted[perm[i]] = i

# Write the inverted permutation, separating each number by a space, and with
# a newline at the end.
temp = ''
for i, v in enumerate(perm_inverted):
    temp += str(v) + ' '
temp = temp[:-1]
stdio.write(temp)
stdio.writeln()
