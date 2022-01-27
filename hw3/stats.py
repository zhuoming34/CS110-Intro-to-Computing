# stats.py: writes the mean, variance, and standard deviation of
# the floats x_1, x_2, \dots, x_n supplied as command-line
# arguments.

import stdio
import sys

# Create a list a consisting of the floats from the command line.
a = sys.argv[1:]
for v in range(1, len(sys.argv)):
    a[v-1] = float(a[v-1])

# Define a variable n and set it to the number of elements in a.
n = len(a)

# Compute the average of a into a variable avg.
avg = 0.0
for v in a:
    avg += int(v)
avg /= n

# Compute the variance of a into a variable var.
var = 0.0
for v in a:
    var += (int(v)-avg)**2
var /= n

# Compute the standard deviation of a into a variable std.
std = var**(0.5)

# Write avg, var, and std.
stdio.writeln(str(avg) + '\n' + str(var) + '\n' + str(std))
