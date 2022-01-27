"""
guitar_string.py

Models a guitar string.
"""

import math
import random
import ring_buffer
import stdarray
import stdio
import sys

# Sampling rate.
SPS = 44100


def create(frequency):
    """
    Create and return a guitar string of the given frequency, using a sampling
    rate given by SPS. A guitar string is represented as a ring buffer of
    of capacity N (SPS divided by frequency, rounded up to the nearest
    integer), with all values initialized to 0.0.
    """

    N = round(SPS / frequency)
    guitar_string = ring_buffer.create(N)
    for i in range(N):
        ring_buffer.enqueue(guitar_string, 0.0)
    return(guitar_string)


def create_from_samples(init):
    """
    Create and return a guitar string whose size and initial values are given
    by the list init.
    """

    N = len(init)
    guitar_string = ring_buffer.create(N)
    for i in range(N):
        ring_buffer.enqueue(guitar_string, init[i])
    return(guitar_string)


def pluck(string):
    """
    Pluck the given guitar string by replacing the buffer with white noise.
    """

    pluck = ring_buffer.dequeue(string)
    ring_buffer.enqueue(string, pluck)


def tic(string):
    """
    Advance the simulation one time step on the given guitar string by applying
    the Karplus-Strong update.
    """

    a = ring_buffer.dequeue(string)
    b = ring_buffer.peek(string)
    KS_num = 0.996 * 0.5 * (a + b)
    ring_buffer.enqueue(string, KS_num)


def sample(string):
    """
    Return the current sample from the given guitar string.
    """

    return(ring_buffer.peek(string))


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)
    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    _main()
