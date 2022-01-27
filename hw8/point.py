import stdio
import sys


class Point:
    """
    Represents a point in 2-dimensional space.
    """

    def __init__(self, x, y):
        """
        Constructs a new point given its x and y coordinates.
        """

        self._x = x
        self._y = y

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between self and other.
        """
        x1 = self._x
        y1 = self._y
        x2 = other._x
        y2 = other._y
        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        return d

    def __str__(self):
        """
        Returns a string representation of self.
        """
        x = self._x
        y = self._y
        return('(' + str(x) + ', ' + str(y) + ')')


# Test client [DO NOT EDIT]. Reads floats x1, y1, x2, y2 from command line,
# constructs two Point objects from them, and writes them along with the
# Euclidean distance between the two.
def _main():
    x1, y1, x2, y2 = map(float, sys.argv[1:])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    stdio.writeln('p1 = ' + str(p1))
    stdio.writeln('p2 = ' + str(p2))
    stdio.writeln('d(p1, p2) = ' + str(p1.distanceTo(p2)))


if __name__ == '__main__':
    _main()
