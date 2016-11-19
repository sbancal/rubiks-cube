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


Rotations are as following :
         ___              ___              ___
       / A /|           / A /|     Z1 →  / A /|
      /__ / |          /__ / |    Zn →  /__ / |
X1 → |   |D |         |   |D |         |   |D |
X2 → | C | /          | C | /          | C | /
Xn → |___|/           |___|/           |___|/
                       ↑↑↑
                       ||Yn
                       |Y2
                       Y1
"""

import re

class Cube():
    """
    Describes the Rubik's cube model with :
        + self.n : the dimension
    """
    def __init__(self, from_file):
        self.faces = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[]}
        self.highlights = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[]}
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
                self.faces[faces[current_face]].append([c for c in l])
                current_face_line += 1
                if current_face_line == self.n:
                    current_face_line = 0
                    current_face += 1
        self.clear_highlights()

    def clear_highlights(self):
        self.highlights = dict([(ltr, [[False for i in range(self.n)] for j in range(self.n)]) for ltr in "ABCDEF"])
        # points = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
        # for ltr in "ABCDEF":
        #     for p in points:
        #         self.highlights[ltr][p[0]][p[1]] = True

    def __str__(self):
        def render_line(ltr, i):
            line = ""
            for j in range(self.n):
                if self.highlights[ltr][i][j]:
                    line += "\033[0;1;93m{}\033[0m".format(self.faces[ltr][i][j])
                else:
                    line += self.faces[ltr][i][j]
            return line

        white = " " * self.n
        s = ""
        for i in range(self.n):
            s += "{white} {a}\n".format(white=white, a=render_line("A", i))
        s += "\n"
        for i in range(self.n):
            s += "{b} {c} {d}\n".format(b=render_line("B", i), c=render_line("C", i), d=render_line("D", i))
        s += "\n"
        for i in range(self.n):
            s += "{white} {e}\n".format(white=white, e=render_line("E", i))
        s += "\n"
        for i in range(self.n):
            s += "{white} {f}\n".format(white=white, f=render_line("F", i))
        s += "\n"
        self.clear_highlights()
        return s
