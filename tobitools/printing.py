#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import codecs
import locale
import math
import sys


def bar_chart(data, maxbarlen=30):
    """
    Prints a bar chart over the given data. The data is expected
    to be a iterable of tuples, where the first element is the
    label and the second element the value of the bar.

    Example:
    >>> print_bar_chart([("A", 32000), ("C", 14000), ("B", 3000)])
    A ██████████████████████████████ 32000
    C ██████████████ 14000
    B ███ 3000
    """
    maxkeylen = max([len(unicode(k)) for k, v in data])
    maxvalue = max([v for k, v in data])
    for k, v in data:
        bar = int(math.ceil((v / float(maxvalue)) * maxbarlen)) * "█"
        print(("%" + unicode(maxkeylen) + "s %s %s") % (k, bar, v))


def set_stdout():
    """
    Sets stdout encoding to the preferred encoding.
    """
    sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)


def stdout(*args):
    """
    Writes the given arguments to stdout and immediately flushes.
    """
    sys.stdout.write(' '.join(map(unicode, args)))
    sys.stdout.flush()
