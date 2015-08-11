#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import os


def walk_files(*args, **kwargs):
    """
    Iterate over all files in the given path(s). If the path
    is a directory, the paths of all files in the directory
    and its subdirectories will be included. If the path is
    a file, the path itself is returned.

    Keyword arguments:
    file_ending: only match files that end with the given ending
                 (case insensitive)
    file_regex: only match files that have a positive `search` match
                in the filename for the given compiled regex object.
    """
    file_ending = kwargs.get("file_ending")
    if file_ending:
        file_ending = file_ending.lower()
    file_regex = kwargs.get("file_regex")

    for path in args:
        assert os.path.exists(path), "Path does not exist: '%s'" % path
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in sorted(filenames):
                    if file_ending and not filename.lower().endswith(file_ending):
                        continue
                    if file_regex and not file_regex.search(filename):
                        continue
                    filepath = os.path.join(dirpath, filename)
                    yield filepath
        else:
            yield path
