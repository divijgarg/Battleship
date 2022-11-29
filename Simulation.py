from OneTrialSimulation import OneTrialSimulation
import pprint


class Simulation:

    def __init__(self, numTrials):
        self.numTrials = numTrials
        self.trials = []

    def createSims(self):
        for i in range(0, self.numTrials):
            self.trials.append(OneTrialSimulation(10, 10, 2, 2, 2, 2, 2))

    def runTrials(self):
        for trial in self.trials:
            trial.createBoards()
            trial.createGamePieces()
            trial.placeGamePieces()
            while not trial.checkIfGameOver():
                trial.doTurn(trial.player1, trial.player2)
                trial.doTurn(trial.player2, trial.player1)

