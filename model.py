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
       / A /|           / A /|     Z0 →  / A /|
      /__ / |          /__ / |    Zn →  /__ / |
X0 → |   |D |         |   |D |         |   |D |
X1 → | C | /          | C | /          | C | /
Xn → |___|/           |___|/           |___|/
                       ↑↑↑
                       ||Yn
                       |Y1
                       Y0
"""

import re
import numpy as np

class Cube():
    """
    Describes the Rubik's cube model with :
        + self.n : the dimension
    """
    def __init__(self, from_file):
        self.faces = {"A":None, "B":None, "C":None, "D":None, "E":None, "F":None}
        self.highlights = {"A":None, "B":None, "C":None, "D":None, "E":None, "F":None}
        self.n = None

        faces = ["A", "B", "C", "D", "E", "F"]
        current_face_id = 0
        current_face_line = 0
        current_face_data = ""
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

                if current_face_id == 6:
                    raise Exception("Error: Found too much data lines in '{}'. Expected {}x6 data lines.".format(
                        from_file, self.n
                    ))
                current_face_data += l
                current_face_line += 1
                if current_face_line == self.n:
                    self.faces[faces[current_face_id]] = np.array(re.findall(r'.', current_face_data)).reshape(self.n, self.n)
                    current_face_line = 0
                    current_face_id += 1
                    current_face_data = ""
        self.clear_highlights()

    def rotate(self, axis, item, direction):
        '''
        Rotates one row on the cube
        axis : 'x' | 'y' | 'z'
        item : num of the row or column to rotate
        direction : True is left->right or bottom->up
        '''
        if axis == 'x':
            if item == 0:
                if direction:
                    k = 1
                else:
                    k = -1
                self.faces["A"] = np.rot90(self.faces["A"], k)
            if direction:
                (self.faces["B"][item,:],
                 self.faces["C"][item,:],
                 self.faces["D"][item,:],
                 self.faces["F"][self.n - item - 1,:]) = (
                 np.flip(np.copy(self.faces["F"][self.n - item - 1,:]),0),
                 np.copy(self.faces["B"][item,:]),
                 np.copy(self.faces["C"][item,:]),
                 np.flip(np.copy(self.faces["D"][item,:]),0))
            else:
                (self.faces["B"][item,:],
                 self.faces["C"][item,:],
                 self.faces["D"][item,:],
                 self.faces["F"][self.n - item - 1,:]) = (
                 self.faces["C"][item,:],
                 self.faces["D"][item,:],
                 np.flip(np.copy(self.faces["F"][self.n - item - 1,:]),0),
                 np.flip(np.copy(self.faces["B"][item,:]),0))
            if item == self.n - 1:
                if direction:
                    k = -1
                else:
                    k = 1
                self.faces["E"] = np.rot90(self.faces["E"], k)


    def clear_highlights(self):
        for ltr in "ABCDEF":
            self.highlights[ltr] = np.full((self.n, self.n), False)
        # points = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), )
        # for ltr in "ABCDEF":
        #     for p in points:
        #         try:
        #             self.highlights[ltr][p[0],p[1]] = True
        #         except IndexError:
        #             pass

    def __str__(self):
        def render_line(ltr, i):
            line = ""
            for j in range(self.n):
                if self.highlights[ltr][i,j]:
                    line += "\033[0;1;93m{}\033[0m".format(self.faces[ltr][i,j])
                else:
                    line += self.faces[ltr][i,j]
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
