#!/usr/bin/env python3

# Bancal Samuel

"""
Provides Evaluator class that will return notes which can be compared then.
Comparing notes between Cubes should indicate if one is closer to be resolved.

Notes are given in a tuple: (a, b, c)
`a` has more weight than `b` which has more weight than `c`

In case the cube is solved, SolvedCubeException is raised.
"""

import numpy as np


class SolvedCubeException(Exception):
    pass


class Evaluator():
    def __init__(self, n):
        self.n = n

        # Prepare eval_indexes
        first_i = int((n-1)/2)
        last_i = int((n)/2)
        self.eval_indexes = []
        if self.n % 2 == 0:
            start = 0
        else:
            start = 1
        for i in range(start, int((n-1)/2)+1):
            self.eval_indexes.append((first_i-i, last_i+i+1))

        self.color_index = first_i
        self.nb_stickers = n*n*6

    def give_a_note(self, cube):
        """
        return a tuple (a, b, ...) where
            + a is the nb of good stickers summed on all faces
                according to self.eval_indexes[0]
            + b is the nb of good stickers summed on all faces
                according to self.eval_indexes[1]
            ...
        It will raise SolvedCubeException when cube is 100% solved
        """
        note = []
        for current_index in self.eval_indexes:
            current_index_note = 0
            for face in cube.faces.values():
                nb_good_stickers = len(np.where(
                    face[current_index[0]:current_index[1],
                         current_index[0]:current_index[1]] ==
                    face[self.color_index, self.color_index])[0])
                current_index_note += nb_good_stickers
            note.append(current_index_note)
        if note[-1] == self.nb_stickers:
            raise SolvedCubeException()
        return tuple(note)
