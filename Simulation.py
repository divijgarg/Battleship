from OneTrialSimulation import OneTrialSimulation
from OneTrialSimulationNew import OneTrialSimulationNew

import pprint

import numpy as np

from matplotlib import pyplot

class Simulation:

    def __init__(self, numTrials):
        self.numTrials = numTrials
        self.trials = []

    def createSims(self):
        for i in range(0, self.numTrials):
            self.trials.append(OneTrialSimulationNew(8, 8, 2, 0, 2, 2, 2))

    def runTrials(self):
        counter=0
        for trial in self.trials:
            counter+=1
            trial.createBoards()
            print("counter")
            print(counter)
            trial.createGamePieces()
            trial.placeGamePieces()
            # for i in range(0,50):
            #     trial.doTurn(trial.player1, trial.player2)
            while not trial.checkIfGameOver():
                trial.doTurn(trial.player1, trial.player2)
                # trial.doTurn(trial.player2, trial.player1)

    # def drawGraph(self,player):

