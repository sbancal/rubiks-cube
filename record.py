#!/usr/bin/env python3

# Bancal Samuel


class Record():
    '''
    Stores an attempt as a record, the link of his parent
    and the links to it's future children.
    Each record has
    + state : how the cube was at that step
      Can be None if we decided to free some memory
    + evaluation : tuple given by evaluator on that cube
    + nbSteps : number of steps to reach that state
    + parent : parent Record
    + opToChild : operation to child Record dict
    '''
    def __init__(self, state, evaluation, parent=None):
        self.state = state
        self.evaluation = evaluation
        self.parent = parent
        if self.parent is None:
            self.nbSteps = 0
        else:
            self.nbSteps = self.parent.nbSteps + 1
        self.opToChild = {}
