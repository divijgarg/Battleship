# coded by Divij Garg

import random
import copy
import statistics
import numpy as np
import pprint
from OneTrialSimulation import OneTrialSimulation





def main():
    test = OneTrialSimulation(10, 10, 2, 2, 2, 2, 2)
    test.createBoards()
    test.createGamePieces()
    test.placeGamePieces()
    pprint.pprint(test.player1Defense)
    pprint.pprint(test.player2Defense)


main()
