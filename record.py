#!/usr/bin/env python3

# Bancal Samuel


class Record():
    '''
    Stores an attempt as a record and the links to it's future children
    Each record has
    + state : how the cube was at that step
      Can be None if we decided to free some memory
    + evaluation : tuple given by evaluator on that cube
    + nbSteps : number of steps to reach that state
    + child : dict of other Records
    '''
    def __init__(self, state, evaluation, nbSteps):
        self.state = state
        self.evaluation = evaluation
        self.nbSteps = nbSteps
        self.child = {}
