import stdio
import sys


class Interval:
    """
    Represents a 1-dimensional interval [lbound, rbound].
    """

    def __init__(self, lbound, rbound):
        """
        Constructs a new interval given its lower and upper bounds.
        """
        self._lbound = lbound
        self._rbound = rbound

    def lbound(self):
        """
        Returns the lower bound of the interval.
        """
        lbound = self._lbound
        return lbound

    def rbound(self):
        """
        Returns the upper bound of the interval.
        """
        rbound = self._rbound
        return rbound

    def contains(self, x):
        """
        Returns True if self contains the point x and False otherwise.
        """
        lbound = self._lbound
        rbound = self._rbound
        if (x >= lbound) and (x <= rbound):
            return True

    def intersects(self, other):
        """
        Returns True if self intersects other and False othewise.
        """
        rbound1 = self._rbound
        lbound2 = other._lbound
        if (rbound1 >= lbound2):
            return True

    def __str__(self):
        """
        Returns a string representation of self.
        """
        lbound = self._lbound
        rbound = self._rbound
        result = '[' + str(lbound) + ', ' + str(rbound) + ']'
        return result


# Test client [DO NOT EDIT]. Reads a float x from the command line and
# writes to standard output: all of the intervals from standard input
# (each defined by a pair of floats) that contain x; and all pairs
# of intervals from standard input that intersect one another.
def _main():
    x = float(sys.argv[1])
    intervals = []
    while not stdio.isEmpty():
        lbound = stdio.readFloat()
        rbound = stdio.readFloat()
        intervals += [Interval(lbound, rbound)]
    for i in range(len(intervals)):
        if intervals[i].contains(x):
            stdio.writef('%s contains %f\n', intervals[i], x)
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                stdio.writef('%s intersects %s\n', intervals[i], intervals[j])


if __name__ == '__main__':
    _main()
