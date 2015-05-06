#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def ngramize(tokens, min_size=1, max_size=1):
    """
    Returns the ngrams from min_size to max_size of the
    given sequence as list of tuples.

    Example:
    >>> list(
        ngramize("colorless green ideas sleep furiously".split(),
                 min_size=1, max_size=2)
    )
    [('colorless',),
     ('colorless', 'green'),
     ('green',),
     ('green', 'ideas'),
     ('ideas',),
     ('ideas', 'sleep'),
     ('sleep',),
     ('sleep', 'furiously'),
     ('furiously',)]
    """
    num_tokens = len(tokens)
    for i in xrange(num_tokens):
        for size in xrange(min_size, max_size + 1):
            if i + size <= num_tokens:
                yield tuple(tokens[i:i + size])
