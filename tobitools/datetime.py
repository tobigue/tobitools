#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import datetime


def nowstr():
    """
    Returns the current date and time as formatted string.
    """
    return "[%s]" % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
