import numpy as np
import unittest
from evaluator import Evaluator

class TestEvaluator(unittest.TestCase):
    def test_eval_matrices_2x2x2(self):
        evaluator = Evaluator(2)
        self.assertEqual(len(evaluator.eval_matrices), 1)
        self.assertEqual(evaluator.eval_matrices[0].tolist(),
            [[ True,  True], [True,  True]])

    def test_eval_matrices_3x3x3(self):
        evaluator = Evaluator(3)
        self.assertEqual(len(evaluator.eval_matrices), 2)
        self.assertEqual(evaluator.eval_matrices[0].tolist(),
            [[False, False, False],
             [False,  True, False],
             [False, False, False]])
        self.assertEqual(evaluator.eval_matrices[1].tolist(),
            [[ True,  True,  True],
             [ True,  True,  True],
             [ True,  True,  True]])

    def test_eval_matrices_4x4x4(self):
        evaluator = Evaluator(4)
        self.assertEqual(len(evaluator.eval_matrices), 2)
        self.assertEqual(evaluator.eval_matrices[0].tolist(),
            [[False, False, False, False],
             [False, True, True, False],
             [False, True, True, False],
             [False, False, False, False]])
        self.assertEqual(evaluator.eval_matrices[1].tolist(),
            [[True, True, True, True],
             [True, True, True, True],
             [True, True, True, True],
             [True, True, True, True]])

    def test_eval_matrices_5x5x5(self):
        evaluator = Evaluator(5)
        self.assertEqual(len(evaluator.eval_matrices), 3)
        self.assertEqual(evaluator.eval_matrices[0].tolist(),
            [[False, False, False, False, False],
             [False, False, False, False, False],
             [False, False, True, False, False],
             [False, False, False, False, False],
             [False, False, False, False, False]])
        self.assertEqual(evaluator.eval_matrices[1].tolist(),
            [[False, False, False, False, False],
             [False, True, True, True, False],
             [False, True, True, True, False],
             [False, True, True, True, False],
             [False, False, False, False, False]])
        self.assertEqual(evaluator.eval_matrices[2].tolist(),
            [[True, True, True, True, True],
             [True, True, True, True, True],
             [True, True, True, True, True],
             [True, True, True, True, True],
             [True, True, True, True, True]])

    def test_eval_matrices_6x6x6(self):
        evaluator = Evaluator(6)
        self.assertEqual(len(evaluator.eval_matrices), 3)
        self.assertEqual(evaluator.eval_matrices[0].tolist(),
            [[False, False, False, False, False, False],
             [False, False, False, False, False, False],
             [False, False, True, True, False, False],
             [False, False, True, True, False, False],
             [False, False, False, False, False, False],
             [False, False, False, False, False, False]])
        self.assertEqual(evaluator.eval_matrices[1].tolist(),
            [[False, False, False, False, False, False],
             [False, True, True, True, True, False],
             [False, True, True, True, True, False],
             [False, True, True, True, True, False],
             [False, True, True, True, True, False],
             [False, False, False, False, False, False]])
        self.assertEqual(evaluator.eval_matrices[2].tolist(),
            [[True, True, True, True, True, True],
             [True, True, True, True, True, True],
             [True, True, True, True, True, True],
             [True, True, True, True, True, True],
             [True, True, True, True, True, True],
             [True, True, True, True, True, True]])
