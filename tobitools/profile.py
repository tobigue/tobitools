#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import sys
import cProfile
import pstats
if sys.version_info < (3,):
    from StringIO import StringIO
else:
    from io import StringIO


class Profiler(object):
    """
    Allows to profile code running in the context of the Profiler.
    Usage:

        from time import sleep
        with Profiler():
            for _ in range(10):
                sleep(0.1)
    """

    def __init__(self, sortby="tottime"):
        self.sortby = sortby

    def __enter__(self):
        self.pr = cProfile.Profile()
        self.pr.enable()

    def __exit__(self, *args):
        self.pr.disable()
        s = StringIO()
        ps = pstats.Stats(self.pr, stream=s).sort_stats(self.sortby)
        ps.print_stats()
        print(s.getvalue())
