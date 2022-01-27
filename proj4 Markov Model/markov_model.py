"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""

import stdio
import stdrandom
import sys
import random


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """

        self._k = k
        self._st = {}
        self._circ_text = text + text[:k]
        ck_text, a, b = [], [], []
        for i in range(len(text)):
            ck_text += [self._circ_text[i:i+k+1]]
        d = {}
        for i in range(len(self._circ_text)-k):
            kgram = self._circ_text[i:i+k]
            c = str(self._circ_text[i+k])
            if str(kgram) not in a:
                a += [kgram]
                d = {}
            else:
                d = self._st.get(kgram)
            if [kgram + c] not in b:
                b += [kgram + c]
                e = [kgram + c]
                j = ck_text.count(e[0])
                d.update({c: j})
                self._st.update({kgram: d})

    def order(self):
        """
        Returns order k of Markov model.
        """
        k = self._k
        return k

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """
        k = self._k
        if k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length '
                             + str(self._k))
        test = self._circ_text + self._circ_text[:k-1]
        ck_text = []
        for i in range(len(self._circ_text)-k):
            ck_text += [self._circ_text[i:i+k]]
        f = ck_text.count(kgram)
        return f

    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length '
                             + str(self._k))
        key = [kgram]
        d = self._st
        char = d.setdefault(key[0])
        if c not in char:
            f = 0
        else:
            f = char.setdefault(c)
        return f

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """
        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)
        return(random.choice(self._circ_text))

    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """
        i = len(self._circ_text) - self._k
        text = self._circ_text[:i]
        for j in range(T):
            new = rand(kgram)
            text += new
        stdio.writeln(text)

    def replace_unknown(self, corrupted):
        """
        Replaces unknown characters (~) in corrupted with most probable
        characters, and returns that string.
        """

        # Given a list a, argmax returns the index of the maximum element in a.
        def argmax(a):
            return a.index(max(a))
        k = self._k
        st = self._st
        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram = corrupted[i-k: i-1]
                d = st.setdefault(kgram)
                char = max(d, key=d.get)
                corrupted.append(corrupted[i].replace('~', char))
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
