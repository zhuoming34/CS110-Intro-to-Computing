import stdio
import sys
from interval import Interval


class Rectangle:
    """
    Represents a rectangle as two (x and y) intervals.
    """

    def __init__(self, xint, yint):
        """
        Constructs a new rectangle given the x and y intervals.
        """
        self._xint = xint
        self._yint = yint

    def area(self):
        """
        Returns the area of self.
        """
        l1 = self._xint._lbound
        r1 = self._xint._rbound
        l2 = self._yint._lbound
        r2 = self._yint._rbound
        d1 = r1 - l1
        d2 = r2 - l2
        area = d1 * d2
        return area

    def perimeter(self):
        """
        Returns the perimeter of self.
        """
        l1 = self._xint._lbound
        r1 = self._xint._rbound
        l2 = self._yint._lbound
        r2 = self._yint._rbound
        d1 = r1 - l1
        d2 = r2 - l2
        perimeter = 2 * (d1 + d2)
        return perimeter

    def contains(self, x, y):
        """
        Returns True if self contains the point (x, y) and False otherwise.
        """
        l1 = self._xint._lbound
        r1 = self._xint._rbound
        l2 = self._yint._lbound
        r2 = self._yint._rbound
        if (x >= l1) and (x <= r1) and (y >= l2) and (y <= r2):
            return True

    def intersects(self, other):
        """
        Returns True if self intersects other and False othewise.
        """
        l1 = self._xint._lbound
        r1 = self._xint._rbound
        l2 = self._yint._lbound
        r2 = self._yint._rbound
        l3 = other._xint._lbound
        r3 = other._xint._rbound
        l4 = other._yint._lbound
        r4 = other._yint._rbound
        if (l1 <= r3) or (r1 >= l3) or (l2 <= r4) or (r2 >= l4):
            return True

    def __str__(self):
        """
        Returns a string representation of self.
        """
        l1 = self._xint._lbound
        r1 = self._xint._rbound
        l2 = self._yint._lbound
        r2 = self._yint._rbound
        result = '[' + str(l1) + ', ' + str(r1) + '] x [' + \
                 str(l2) + ', ' + str(r2) + ']'
        return result


# Test client [DO NOT EDIT]. Reads a floats x and y from the command line and
# writes to standard output: all of the rectangles from standard input
# (each defined by two pairs of floats) that contain (x, y); and all pairs
# of rectangles from standard input that intersect one another.
def _main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    rectangles = []
    while not stdio.isEmpty():
        lbound1 = stdio.readFloat()
        rbound1 = stdio.readFloat()
        lbound2 = stdio.readFloat()
        rbound2 = stdio.readFloat()
        rectangles += [Rectangle(Interval(lbound1, rbound1),
                                 Interval(lbound2, rbound2))]
    for i in range(len(rectangles)):
        stdio.writef('Area(%s) = %f\n', rectangles[i], rectangles[i].area())
        stdio.writef('Perimeter(%s) = %f\n', rectangles[i],
                     rectangles[i].perimeter())
        if rectangles[i].contains(x, y):
            stdio.writef('%s contains (%f, %f)\n', rectangles[i], x, y)
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                stdio.writef('%s intersects %s\n',
                             rectangles[i], rectangles[j])


if __name__ == '__main__':
    _main()
