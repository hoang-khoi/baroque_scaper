#!/usr/bin/env python3
__author__ = "Khoi"
__version__ = "0.1.0"
__license__ = "MIT"

import pathlib
import sys

from baroque_scaper.baroque_scraper_impl import BaroqueScaperImpl


def main():
    """ Main entry point of the app """
    path = pathlib.Path().absolute()
    if len(sys.argv) > 1:
        path = pathlib.Path(sys.argv[1])

    baroque_scraper = BaroqueScaperImpl()
    baroque_scraper.scrape(path)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
