"""
ring_buffer.py

Models a ring buffer.
"""

import stdarray
import stdio
import sys


def create(capacity):
    """
    Create and return a ring buffer, with the given maximum capacity and
    with all elements initialized to None. A ring buffer is represented as
    a list of four elements: the buffer (buff) itself as a list; number of
    elements (size) currently in buff; the index (first) of the least
    recently inserted item; and the index (last) one beyond the most recently
    inserted item.
    """
    rb = []
    buff = [None] * capacity
    rb.append(buff)
    rb.append(0)
    rb.append(0)
    rb.append(0)
    return(rb)


def capacity(rb):
    """
    Return the capacity of the ring buffer.
    """
    capacity = len(rb[0])
    return(capacity)


def size(rb):
    """
    Return the number of items currently in the buffer rb.
    """
    size = 0
    for v in rb[0]:
        if v is not None:
            size += 1
    return(size)


def is_empty(rb):
    """
    Return True if the buffer rb is empty and False otherwise.
    """
    if size(rb) == 0:
        return('True')
    else:
        return('False')


def is_full(rb):
    """
    Return True if the buffer rb is full and False otherwise.
    """
    if size(rb) == len(rb[0]):
        return('True')
    else:
        return('False')


def enqueue(rb, x):
    """
    Add item x to the end of the buffer rb.
    """
    if is_full(rb) == 'True':
        msg = 'Error: cannot enqueue a full buffer'
        sys.exit(msg)
    rb[0][rb[3]] = x
    rb[3] += 1
    if rb[3] == len(rb[0]):
        rb[3] = 0
    rb[1] = size(rb)
    return(rb)


def dequeue(rb):
    """
    Delete and return item from the front of the buffer rb.
    """
    if is_empty(rb) == 'True':
        msg = 'Error: cannot dequeue an empty buffer'
        sys.exit(msg)
    first = rb[0][rb[2]]
    rb[0][rb[2]] = None
    rb[2] += 1
    if rb[2] == len(rb[0]):
        rb[2] = 0
    rb[1] = size(rb)
    return(first)


def peek(rb):
    """
    Return (but do not delete) item from the front of the buffer rb.
    """
    if is_empty(rb) == 'True':
        msg = 'Error: cannot peek an empty buffer'
        sys.exit(msg)
    first = rb[0][rb[2]]
    return(first)


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    _main()
