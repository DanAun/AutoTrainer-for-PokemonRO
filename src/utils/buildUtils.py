import os
import sys


def resourcePath(relative_path):
    """ Get the path to the resource, works for both development and compiled versions. """
    try:
        # PyInstaller stores the path in sys._MEIPASS when running from a bundled executable
        base_path = sys._MEIPASS
    except Exception:
        # In development mode, resources are in the current working directory
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
