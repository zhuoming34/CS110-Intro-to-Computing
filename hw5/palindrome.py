import stdio
import sys


# Return True if s is a palindrome and False otherwise. You may assume that
# s is all lower case and doesn't any whitespace characters.
def is_palindrome(s):
    # Iterate over half of the string s. Compare character at i with
    # the character at len(s) - i - 1. If they are different, return False
    # Otherwise, continue. Return True when the loop is exhausted.
    j = len(s)
    if j % 2 == 0:
        j = j // 2
    else:
        j = (j // 2) + 1
    for i in range(j):
        if (s[i] != s[len(s)-i-1]):
            return('False')
    return('True')


# Test client [DO NOT EDIT]. Reads a string s as command-line argument and
# prints True if s is a palindrome, ie, reads the same forwards and backwards,
# and False otherwise.
def _main():
    s = sys.argv[1]
    stdio.writeln(is_palindrome(s))


if __name__ == '__main__':
    _main()
