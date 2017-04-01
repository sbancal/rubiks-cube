#!/usr/bin/env python3

# Bancal Samuel

"""
Provides Evaluator class that will return notes which can be compared then.
Comparing notes between Cubes should indicate if one is closer to be resolved.
"""

import numpy as np

class Evaluator():
    def __init__(self, n):
        self.n = n

        #Prepare eval_matrices
        first_i = int((n-1)/2)
        last_i = int((n)/2)
        self.eval_matrices = []
        for i in range(int((n-1)/2)+1):
            mat = np.zeros((n,n), dtype=np.bool)
            mat[first_i-i:last_i+i+1,first_i-i:last_i+i+1] = True
            self.eval_matrices.append(mat)
