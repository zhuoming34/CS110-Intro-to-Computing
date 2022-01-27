# name_age.py: takes two strings name and age as command-line arguments and
# writes the output "name is age years old.".

import stdio
import sys

# Get name from command line.
name = sys.argv[1]

# Get age from command line.
age = sys.argv[2]

print(name, ' is ', age, ' years old.', sep='')
