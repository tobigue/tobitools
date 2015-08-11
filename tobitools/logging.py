#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys


def stderr_logging():
    """
    Adds a stderr stream handler to the root logger.
    """
    logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))
