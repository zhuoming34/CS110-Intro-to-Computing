import stdio
import sys


# Returns the domain type of the given URL.
def domain_type(URL):
    url1 = URL[7:]
    i = url1.find('/')
    url2 = url1[:i]
    url3 = url2.split('.')
    return(url3[-1])


# Test client [DO NOT EDIT]. Reads a URL as command-line argument and writes
# its domain type.
def _main():
    URL = sys.argv[1]
    stdio.writeln(domain_type(URL))


if __name__ == '__main__':
    _main()
