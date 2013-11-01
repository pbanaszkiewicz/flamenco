# coding: utf-8

"""Flamenco -- static pages generator, mostly intended for blogs.

Usage:
  flamenco quickgen
  flamenco compile [--config=PATH]
  flamenco help <command>
  flamenco -h | --help
  flamenco --version

Options:
  -c PATH, --config=PATH        Configuration file path.
  -h, --help                    This help text.
  --version                     Show version.
"""

from __future__ import print_function
from . import __version__ as VERSION
from docopt import docopt


def cli():
    print(docopt(__doc__, version=VERSION))
