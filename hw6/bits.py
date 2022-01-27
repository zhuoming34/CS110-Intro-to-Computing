import stdio
import sys


# Return the number of zeros in s, computed recursively.
def zeros(s):
    if (len(s) == 0):
        return(0)
    elif (len(s) == 1):
        if (s[0] == '0'):
            return(1)
        elif (s[0] == '1'):
            return(0)
    elif (s[0] == '0'):
        return(1 + zeros(s[1:]))
    elif (s[0] == '1'):
        return(0 + zeros(s[1:]))


# Return the number of ones in s, computed recursively.
def ones(s):
    if (len(s) == 0):
        return(0)
    elif (len(s) == 1):
        if (s[0] == '0'):
            return(0)
        elif (s[0] == '1'):
            return(1)
    elif (s[0] == '0'):
        return(0 + ones(s[1:]))
    elif (s[0] == '1'):
        return(1 + ones(s[1:]))


# Test client [DO NOT EDIT]. Reads a string s from command line and writes the
# the number of zeros and ones in s, both computed recursively.
def _main():
    s = sys.argv[1]
    stdio.writef('zeros = %d, ones = %d, total = %d\n',
                 zeros(s), ones(s), len(s))


if __name__ == '__main__':
    _main()
