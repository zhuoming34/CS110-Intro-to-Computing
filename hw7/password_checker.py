import stdio
import sys


# Returns True if pwd is a valid password and False otherwise.
def is_valid(pwd):
    if (len(pwd) < 8) or pwd.isdigit() \
       or pwd.isupper() or pwd.islower() \
       or pwd.isalnum():
        return('False')
    else:
        return('True')


# Test client [DO NOT EDIT]. Reads a password string as command-line argument
# and writes True if it's valid and False otherwise.
def _main():
    pwd = sys.argv[1]
    stdio.writeln(is_valid(pwd))


if __name__ == '__main__':
    _main()
