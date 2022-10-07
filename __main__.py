#!/usr/bin/env python3
__author__ = "Khoi"
__version__ = "0.1.0"
__license__ = "MIT"

import pathlib

from baroque_scaper.baroque_scraper_impl import BaroqueScaperImpl


def main():
    """ Main entry point of the app """
    baroque_scaper = BaroqueScaperImpl()
    baroque_scaper.scap(pathlib.Path().absolute())


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
