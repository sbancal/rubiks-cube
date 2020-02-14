#!/usr/bin/env python3

# Bancal Samuel

"""
Solves rubik's cube given in parameter
"""

import model
import argparse


def parse_arguments():
    """
        Parse arguments and return them
    """
    options = {
        "filename": None,
    }
    parser = argparse.ArgumentParser(description="Solves rubik's cube")
    parser.add_argument("filename", metavar="f", type=str,
                        help="a filename containing a Rubik's cube to solve")
    args = parser.parse_args()
    options["filename"] = args.filename
    return options


if __name__ == "__main__":
    print("Going to solve Rubik's cube ...")
    options = parse_arguments()
    cube = model.Cube(options["filename"])
    print(cube)
    print("Done. (well not yet ;)")
