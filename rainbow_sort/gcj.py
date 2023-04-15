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
3 8 2 8 1


observation: same colours must be batched next to each other.
if i encounter a card before and it moved on, then i cannot encounter the card again.

set a set of prevs
3 -> not encountered before, or previous one is also 3. place.
8 -> not encountered before.
2 -> not encountered before
8 -> encountered before

3 8 8 2
3 -> not encountered before
8 -> not encountered before
8 -> same as previous, so it's counted
2 -> not encountered before

edge case:
3 8 8 2 8 

so i disqualify if:
it is encountered before AND it is not the same as the previous object. 
if it's qualified, but encountered before, i ignore
if it's qualified and not encountered before, i add it to the list.
return string join.
'''

def readcase(f):
    _ = readline(f) # ignore number, I don't need this
    return readints(f, sep=" ")

def solve(c):
    encountered = set()
    cards = []
    for num in c:
        if num in encountered:
            if num != cards[-1]:
                return "IMPOSSIBLE"
        else:
            encountered.add(num)
            cards.append(num)
    return strjoin(cards) if len(cards) == len(set(c)) else "IMPOSSIBLE"


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