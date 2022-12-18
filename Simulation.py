from OneTrialSimulationNew import OneTrialSimulationNew
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statistics import mode


def findLongest(array, value):
    length = 0
    location = 0
    i = -1
    while i < len(array):
        i += 1
        current = 0
        while i < len(array) and array[i] == value:
            current += 1
            i += 1
        if current > length:
            length = current
            location = i - length

    return [length, location]


def createScatterPlot(xArray, yArray, title, xLabel, yLabel):
    plt.title(title)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.scatter(xArray, yArray, s=10, alpha=0.1)
    plt.show()


def createLinePlot(xArray, yArray, title, xLabel, yLabel):
    plt.title(title)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.plot(xArray, yArray)
    plt.show()


def createHistogram(array, x, y, title):
    fig, ax = plt.subplots(figsize=(10, 7))
    bins = list(range(np.min(array), np.max(array) + 1))
    ax.hist(array, bins=bins)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    # Show plot
    plt.show()


def createBarGraph(xarray, data, x, y, title):
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    # Show plot
    plt.bar(xarray, data)
    plt.show()


class Simulation:

    def __init__(self, numTrials):
        self.numTrials = numTrials
        self.trials = []

    def createSims(self):
        for i in range(0, self.numTrials):
            self.trials.append(OneTrialSimulationNew(10, 10, 2, 4, 0, 2, 2))

    def runTrials(self):
        counter = 0
        for trial in self.trials:
            if counter % 100 == 0: print(counter)
            counter += 1
            trial.createBoards()
            trial.createGamePieces()
            trial.placeGamePieces()
            while not trial.checkIfGameOver():
                trial.player1.numberOfMoves += 1
                trial.doTurn(trial.player1, trial.player2)
                if not trial.checkIfGameOver():
                    trial.player2.numberOfMoves += 1
                    trial.doTurn(trial.player2, trial.player1)

    def doStatsAnalysis(self):
        numberMovesPlayer1 = []
        successfulAttacksPlayer1 = []
        failedAttacksPlayer1 = []
        totalAttacksPlayer1 = []
        player1AttackSequences = []
        player1MoveSequences = []
        player1DestructionOrders = []
        for i in self.trials:
            p1 = i.player1
            numberMovesPlayer1.append(p1.numberOfMoves)
            successfulAttacksPlayer1.append(p1.recordOfAttacks.count(True))
            failedAttacksPlayer1.append(p1.recordOfAttacks.count(False))
            totalAttacksPlayer1.append(len(p1.recordOfAttacks))

            player1AttackSequences.append(p1.recordOfAttacks)
            player1MoveSequences.append(p1.recordOfMoves)
            player1DestructionOrders.append(p1.orderOfDestruction)

        self.statsOnDestructionPattern(numberMovesPlayer1, player1DestructionOrders)
        self.statsOnProbabilities(numberMovesPlayer1, player1AttackSequences, player1MoveSequences)
        self.statsOnAttacks(successfulAttacksPlayer1, failedAttacksPlayer1, totalAttacksPlayer1, numberMovesPlayer1)
        self.longestAttackSequence(player1AttackSequences, numberMovesPlayer1)

    def statsOnDestructionPattern(self, numberMoves, destruction):
        firstsCounts = [0, 0, 0, 0]
        lastsCounts = [0, 0, 0, 0]
        movesPerFirst = [0, 0, 0, 0]
        amountMovesPerFirst = [0, 0, 0, 0]
        firsts = []
        lasts = []
        for i in range(0, len(destruction)):
            if len(destruction[i])>0 and destruction[i][0] - 2 >= 0:
                firstsCounts[destruction[i][0] - 2] += 1
                lastsCounts[destruction[i][len(destruction[i]) - 1] - 2] += 1

                movesPerFirst[destruction[i][0] - 2] += numberMoves[i]
                amountMovesPerFirst[destruction[i][0] - 2] += 1

                firsts.append(destruction[i][0])
                lasts.append(destruction[i][len(destruction[i]) - 1])

        for i in range(0, len(movesPerFirst)):
            movesPerFirst[i] = movesPerFirst[i] / amountMovesPerFirst[i]

        createBarGraph([2, 3, 4, 5], firstsCounts, "Length of First Ship Destroyed ", "Amount",
                       "Lengths of First Ship Destroyed")
        createBarGraph([2, 3, 4, 5], lastsCounts, "Length of Last Ship Destroyed ", "Amount",
                       "Lengths of Last Ship Destroyed")
        createLinePlot([2, 3, 4, 5], movesPerFirst, "How the first Ship Attacked Affects Length of Game",
                       "First ship hit", "Average Number of Moves")

    def statsOnProbabilities(self, numberMoves, attackSequences, moveSequences):
        modeOfMoves = mode(numberMoves)
        successes = [0 for _ in range(0, modeOfMoves)]
        totalAttempts = [0 for _ in range(0, modeOfMoves)]
        # print(attackSequences)
        # print(moveSequences)

        counter = 0
        for game in range(0, len(numberMoves)):
            if numberMoves[game] == modeOfMoves:
                counter += 1
                for i in range(0, len(moveSequences[game])):
                    index = moveSequences[game][i] - 1
                    totalAttempts[index] += 1
                    if attackSequences[game][i]:
                        successes[moveSequences[game][i] - 1] += 1

        for i in range(0, len(successes)):
            successes[i] = successes[i] / counter
            totalAttempts[i] = totalAttempts[i] / counter

        # print(counter)
        # print(successes)
        # print(totalAttempts)

        createLinePlot([i for i in range(1, modeOfMoves + 1)], totalAttempts, " Average sequence on each turn", "Turn",
                       "Sequence Length")

    def statsOnAttacks(self, success, failed, total, moves):
        percentSuccessful = []
        for i in range(0, len(success)):
            percentSuccessful.append(success[i] / (total[i]))

        # print(percentSuccessful)
        createScatterPlot(moves, percentSuccessful, "Number of Moves vs Success Rate of Attacks",
                          "Number of Moves", "Success Rate of Attacks")

    def longestAttackSequence(self, attackSequences, numberOfMoves):
        lengthsOfLongestSequence = []
        locationsOfLongestSequence = []
        for seq in attackSequences:
            data = findLongest(seq, True)
            lengthsOfLongestSequence.append(data[0])
            locationsOfLongestSequence.append(data[1])

        # print(lengthsOfLongestSequence)

        print(stats.describe(lengthsOfLongestSequence))

        createHistogram(lengthsOfLongestSequence, "Length of Sequence", "Amount",
                        "Number of times longest sequence occurs")
        createScatterPlot(numberOfMoves, lengthsOfLongestSequence, "Number of Moves vs Length of Longest Sequence",
                          "Number of Moves", "Length of Sequence")
        createScatterPlot(locationsOfLongestSequence, lengthsOfLongestSequence,
                          "Move Sequence Happened vs Length of Sequence",
                          "Move Happened", "Length of Sequence")
