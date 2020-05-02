import unittest
from record import Record


class TestRecord(unittest.TestCase):
    def test_creation(self):
        state = 'state'
        evaluation = (1, 2, 3)
        parent = None
        rec = Record(state, evaluation, parent)
        self.assertEqual(rec.state, state)
        self.assertEqual(rec.evaluation, evaluation)
        self.assertEqual(rec.parent, parent)
        self.assertEqual(rec.nbSteps, 0)
        self.assertEqual(rec.opToChild, {})

    def test_2children(self):
        parent = {
            'state': 'state',
            'evaluation': (1, 2, 3),
            'parent': None,
        }
        recParent = Record(**parent)
        children = [
            {
                'state': 'state child1',
                'evaluation': (2, 3, 4),
                'parent': recParent,
            },
            {
                'state': 'state child2',
                'evaluation': (3, 4, 5),
                'parent': recParent,
            },
        ]
        recParent.opToChild[('x', 0, True)] = Record(**children[0])
        recParent.opToChild[('x', 0, False)] = Record(**children[1])
        self.assertEqual(len(recParent.opToChild), 2)
        self.assertEqual(
            recParent.opToChild['x', 0, True].state, children[0]['state'])
        self.assertEqual(recParent.opToChild['x', 0, True].nbSteps, 1)
        self.assertEqual(recParent.opToChild['x', 0, False].nbSteps, 1)
        self.assertEqual(recParent.opToChild['x', 0, False].parent, recParent)
