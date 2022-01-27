# mercator.py: Takes three floats Lambda0, Phi, and Lambda as command-line
# arguments and prints its projection, i.e., the x and y values separated
# by a space, calculated using x=Lambda-Lambda0 and
# y=ln((1+sin(Phi))/(1-sin(Phi)))/2.

import math
import stdio
import sys

Lambda0 = float(sys.argv[1])
Phi = float(sys.argv[2])
Lambda = float(sys.argv[3])

Phi = math.radians(Phi)

x = Lambda - Lambda0
y = math.log((1 + math.sin(Phi)) / (1 - math.sin(Phi))) / 2

print(x, y)
