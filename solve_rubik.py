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
    parser.add_argument("filename", type=str,
                        help="a filename containing a Rubik's cube to solve")
    args = parser.parse_args()
    options["filename"] = args.filename
    return options


if __name__ == "__main__":
    options = parse_arguments()
    print("Going to solve Rubik's cube ...")
    cube = model.Cube(options["filename"])
    print(cube)
    print("Done. (well not yet ;)")
