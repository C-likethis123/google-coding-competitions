#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
http://bit.ly/1O2UcwC
'''

import bisect
import collections
import collections.abc
import itertools
import math
import re
import sys

from pprint import pprint


# ------------------------
# Be creative here
# ------------------------

'''
ABCD...XYZ

what is the Nth printed letter without waiting for it to be printed?
some ideas:
I have an index.
First round: 26 letters
Second round: 26 * 2 = 52 letters
Third round: 26 * 3 = 78 letters

What I can do:
31 - 26 = 5 ->
then num repetitions += 1
since 5 < 26 * num repetitions, 
I know that it starts at the sequence AABB...
then map it to a letter via some math.
ceil(5 / 2) = 2 -> this would map to C if I do ord('A') + floor(5/2)
AABBCC
123456

ABCDEF
123456
'''

ALPHABET_LENGTH = 26

def readcase(f):
    return readint(f)

def solve(c):
    reps = 1
    seq_length = ALPHABET_LENGTH
    while c > seq_length:
        c -= seq_length
        reps += 1
        seq_length += ALPHABET_LENGTH

    return chr(ord('A') + math.ceil(c / reps) - 1)


# ------------------------
# No touchy
# ------------------------

class InputReader(collections.abc.Iterable):

    _cases = None

    def __init__(self, reader, inp=None):
        self._read(reader, inp or sys.stdin)

    def _read(self, reader, inp):
        t = int(next(inp))
        self._cases = [reader(inp) for _ in range(t)]
        assert len(self._cases) == t

    def __iter__(self):
        return iter(self._cases)


def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))


# ------------------------
# Utilities
# ------------------------

def has_duplicates(lst):
    return len(lst) != len(set(lst))

def bsearch(a, x):
    '''
    Locate the leftmost value exactly equal to x.
    https://docs.python.org/3/library/bisect.html#module-bisect
    '''
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError


def defdict(x=0):
    return collections.defaultdict(lambda: x)


def mapadd(xs, y):
    return [x + y for x in xs]


def readint(f):
    return int(readline(f))


def readints(f, expected=None, sep=None):
    line = readline(f)
    xs = [int(e) for e in line.split(sep)]
    if expected is not None:
        assert len(xs) == expected, '{} != {}'.format(len(xs), expected)
    return xs


def readline(f):
    return next(f).strip()


def rwh_primes2(n):
    '''
    Input n >= 6, returns a list of primes, 2 <= p < n.
    http://stackoverflow.com/revisions/33356284/2
    '''
    # TODO: Silence PEP8's E221 warning.
    zero  = bytearray([0])
    size  = n // 3 + (n % 6 == 2)
    sieve = zero + bytearray([1]) * (size - 1)
    top   = int(math.sqrt(n)) // 3
    for i in range(top + 1):
        if sieve[i]:
            k     = (3*i + 1) | 1
            ksq   = k * k
            k2    = k * 2
            start = (ksq + k2 * (2 - (i & 1))) // 3
            ksqd3 = ksq // 3
            sieve[ksqd3::k2] = zero * ((size - ksqd3 - 1) // k2 + 1)
            sieve[start::k2] = zero * ((size - start - 1) // k2 + 1)
    ans = [2, 3]
    poss = itertools.chain.from_iterable(
        itertools.zip_longest(*[range(i, n, 6) for i in (1, 5)])
    )
    ans.extend(itertools.compress(poss, sieve))
    return ans


def strjoin(xs, glue=' ', conv=str):
    return glue.join(map(conv, xs))


if __name__ == '__main__':
    main()