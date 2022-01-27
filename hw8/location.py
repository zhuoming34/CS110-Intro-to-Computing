import math
import stdio
import sys


class Location:
    """
    Represents a location on Earth.
    """

    def __init__(self, lat, lon):
        """
        Constructs a new location given its latitude and longitude values.
        """
        self._lat = lat
        self._lon = lon

    def distanceTo(self, other):
        """
        Returns the great-circle distance between self and other.
        """
        lat1 = self._lat
        lon1 = self._lon
        lat2 = other._lat
        lon2 = other._lon
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        x1 = math.radians(lat1)
        y1 = math.radians(lon1)
        x2 = math.radians(lat2)
        y2 = math.radians(lon2)
        a = math.sin(x1) * math.sin(x2)
        b = math.cos(x1) * math.cos(x2) * math.cos(y1-y2)
        d = 111 * math.degrees(math.acos(a + b))
        return (d)

    def __str__(self):
        """
        Returns a string representation of self.
        """
        lat = self._lat
        lon = self._lon
        result = '(' + str(lat) + ', ' + str(lon) + ')'
        return (result)


# Test client [DO NOT EDIT]. Reads floats lat1, lon1, lat2, lon2 from command
# representing two locations on Earth, constructs two Location objects from
# them, and writes them along with the great-circle distance between the two.
def _main():
    lat1, lon1, lat2, lon2 = map(float, sys.argv[1:])
    loc1 = Location(lat1, lon1)
    loc2 = Location(lat2, lon2)
    stdio.writeln('loc1 = ' + str(loc1))
    stdio.writeln('loc2 = ' + str(loc2))
    stdio.writeln('d(loc1, loc2) = ' + str(loc1.distanceTo(loc2)))


if __name__ == '__main__':
    _main()
