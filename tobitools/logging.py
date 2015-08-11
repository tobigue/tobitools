#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging
import sys


def stderr_logging():
    """
    Adds a stderr stream handler to the root logger.
    """
    logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))
