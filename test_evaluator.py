import unittest
import numpy as np
from model import Cube
from evaluator import Evaluator, SolvedCubeException

class TestEvaluatorEvalMatrices(unittest.TestCase):
    def test_eval_indexes_2x2x2(self):
        evaluator = Evaluator(2)
        self.assertEqual(len(evaluator.eval_indexes), 1)
        self.assertEqual(evaluator.eval_indexes[0], (0, 2))

    def test_eval_indexes_3x3x3(self):
        evaluator = Evaluator(3)
        self.assertEqual(len(evaluator.eval_indexes), 1)
        self.assertEqual(evaluator.eval_indexes[0], (0, 3))

    def test_eval_indexes_4x4x4(self):
        evaluator = Evaluator(4)
        self.assertEqual(len(evaluator.eval_indexes), 2)
        self.assertEqual(evaluator.eval_indexes[0], (1, 3))
        self.assertEqual(evaluator.eval_indexes[1], (0, 4))

    def test_eval_indexes_5x5x5(self):
        evaluator = Evaluator(5)
        self.assertEqual(len(evaluator.eval_indexes), 2)
        self.assertEqual(evaluator.eval_indexes[0], (1, 4))
        self.assertEqual(evaluator.eval_indexes[1], (0, 5))

    def test_eval_indexes_6x6x6(self):
        evaluator = Evaluator(6)
        self.assertEqual(len(evaluator.eval_indexes), 3)
        self.assertEqual(evaluator.eval_indexes[0], (2, 4))
        self.assertEqual(evaluator.eval_indexes[1], (1, 5))
        self.assertEqual(evaluator.eval_indexes[2], (0, 6))


class TestEvaluatorGiveANote(unittest.TestCase):
    def test_give_a_note_on_random1(self):
        cube = Cube('random1.txt')
        evaluator = Evaluator(3)
        self.assertEqual(evaluator.give_a_note(cube), (18,))

    def test_give_a_note_on_6_random1(self):
        cube = Cube('6_random1.txt')
        evaluator = Evaluator(6)
        self.assertEqual(evaluator.give_a_note(cube), (12, 35, 84))

    def test_give_a_note_on_3x3x3_solved(self):
        cube = Cube('3x3x3_solved.txt')
        evaluator = Evaluator(3)
        with self.assertRaises(SolvedCubeException):
            evaluator.give_a_note(cube)
