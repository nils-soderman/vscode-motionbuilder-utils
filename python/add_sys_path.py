""" Script to add the given paths to sys.path """

import sys
import os


def main(paths):
    # Sort the paths by length to ensure that the most specific paths are added first
    paths.sort(key=len, reverse=True)

    for vsc_path in paths:
        normalized_path = os.path.normpath(vsc_path)
        # Make sure the path doesn't already exist in sys.path
        if not any(normalized_path.lower() == os.path.normpath(path).lower() for path in sys.path):
            sys.path.append(normalized_path)
            print('Added "%s" to sys.path' % normalized_path)
