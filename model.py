#!/usr/bin/env python3

# Bancal Samuel

"""
Describes the Rubik's cube model

2-D representation looks like this :
    A
  B C D
    E
    F

File's format should look like :

A1A2A3
A4A5A6
A7A8A9
B1B2B3
B4B5B6
B7B8B9
C1C2C3
C4C5C6
C7C8C9
...
"""

import re

class Cube():
    """
    Describes the Rubik's cube model with :
        + self.n : the dimension
    """
    def __init__(self, from_file):
        self.faces = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[]}
        self.n = None

        faces = ["A", "B", "C", "D", "E", "F"]
        current_face = 0
        current_face_line = 0
        with open(from_file, "r") as f:
            for line in f.readlines():
                l = re.sub(r"#.*$", "", line).strip()
                if l == '':
                    continue
                if self.n is None:
                    self.n = len(l)
                else:
                    if len(l) != self.n:
                        raise Exception("Error parsing '{}' file."
                            "Doesn't seems to have a clear 'n' : {} != {}".format(
                                from_file, self.n, len(l)
                            ))

                if current_face == 6:
                    raise Exception("Error: Found too much data lines in '{}'. Expected {}x6 data lines.".format(
                        from_file, self.n
                    ))
                self.faces[faces[current_face]].append(re.findall(r".", l))
                current_face_line += 1
                if current_face_line == self.n:
                    current_face_line = 0
                    current_face += 1

    def __str__(self):
        white = " " * self.n
        s = ""
        for i in range(self.n):
            s += "{white} {a}\n".format(white=white, a="".join(self.faces["A"][i]))
        s += "\n"
        for i in range(self.n):
            s += "{b} {c} {d}\n".format(b="".join(self.faces["B"][i]), c="".join(self.faces["C"][i]), d="".join(self.faces["D"][i]))
        s += "\n"
        for i in range(self.n):
            s += "{white} {e}\n".format(white=white, e="".join(self.faces["E"][i]))
        s += "\n"
        for i in range(self.n):
            s += "{white} {f}\n".format(white=white, f="".join(self.faces["F"][i]))
        s += "\n"
        return s
