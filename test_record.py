import unittest
from record import Record


class TestRecord(unittest.TestCase):
    def test_creation(self):
        state = 'state'
        evaluation = (1, 2, 3)
        nbSteps = 0
        rec = Record(state, evaluation, nbSteps)
        self.assertEqual(rec.state, state)
        self.assertEqual(rec.evaluation, evaluation)
        self.assertEqual(rec.nbSteps, nbSteps)
        self.assertEqual(rec.child, {})

    def test_2children(self):
        parent = {
            'state': 'state',
            'evaluation': (1, 2, 3),
            'nbSteps': 0
        }
        children = [
            {
                'state': 'state child1',
                'evaluation': (2, 3, 4),
                'nbSteps': 1,
            },
            {
                'state': 'state child2',
                'evaluation': (3, 4, 5),
                'nbSteps': 1,
            },
        ]
        recParent = Record(**parent)
        recParent.child[('x', 0, True)] = Record(**children[0])
        recParent.child[('x', 0, False)] = Record(**children[1])
        self.assertEqual(len(recParent.child), 2)
        self.assertEqual(
            recParent.child['x', 0, True].state, children[0]['state'])
