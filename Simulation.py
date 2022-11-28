from OneTrialSimulation import OneTrialSimulation
import pprint


class Simulation:

    def __init__(self, numTrials):
        self.numTrials = numTrials
        self.trials = []

    def createSims(self):
        for i in range(0, self.numTrials):
            self.trials.append(OneTrialSimulation(10, 10, 1, 1, 1, 1, 1))

    def runTrials(self):
        for trial in self.trials:
            trial.createBoards()
            trial.createGamePieces()
            trial.placeGamePieces()
            trial.doTurn(trial.player1, trial.player2)

