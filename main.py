# coded by Divij Garg

import random
import copy
import statistics
import numpy as np
import pprint


class GamePiece:
    def __init__(self, numPlacesOccupied):
        self.numPlacesOccupied = numPlacesOccupied
        self.coordinates = []
        self.attackedCoordinates = []
        self.orientation = -2  # 0 is down, 1 is right

    def returnLength(self):
        return self.numPlacesOccupied

    # stores the coordinates that the ship will occupy
    def setCoordinates(self, startingX, startingY, orient, gameBoard):
        self.orientation = orient
        if orient == 0:
            for i in range(0, self.numPlacesOccupied):
                self.coordinates.append([startingX, startingY + i])
                gameBoard[startingX][startingY + i] = self.numPlacesOccupied
        else:
            for i in range(0, self.numPlacesOccupied):
                self.coordinates.append([startingX + i, startingY])
                gameBoard[startingX + i][startingY] = self.numPlacesOccupied
        for i in range(0, self.numPlacesOccupied):
            self.attackedCoordinates.append(False)


class OneTrialSimulation:

    def __init__(self, xDimen, yDimen, numDestroyer, numCruiser, numSubmarine, numBattleship, numCarrier):
        self.yDimen = yDimen
        self.xDimen = xDimen
        self.player1Defense = []
        self.player1Attack = []
        self.player2Defense = []
        self.player2Attack = []
        self.player1Pieces = []
        self.player2Pieces = []
        self.numDestroyer = numDestroyer
        self.numCruiser = numCruiser
        self.numCarrier = numCarrier
        self.numBattleship = numBattleship
        self.numSubmarine = numSubmarine

    # creates the 10 x 10 game board for the game
    def createBoards(self):
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player1Defense.append(arr)
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player1Attack.append(arr)
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player2Defense.append(arr)
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player2Attack.append(arr)

    # creates objects to represent all of the game pieces
    def createGamePieces(self):
        for i in range(0, self.numDestroyer):
            self.player1Pieces.append(GamePiece(2))
            self.player2Pieces.append(GamePiece(2))
        for i in range(0, self.numCruiser):
            self.player1Pieces.append(GamePiece(3))
            self.player2Pieces.append(GamePiece(3))
        for i in range(0, self.numSubmarine):
            self.player1Pieces.append(GamePiece(3))
            self.player2Pieces.append(GamePiece(3))

        for i in range(0, self.numBattleship):
            self.player1Pieces.append(GamePiece(4))
            self.player2Pieces.append(GamePiece(4))

        for i in range(0, self.numCarrier):
            self.player1Pieces.append(GamePiece(5))
            self.player2Pieces.append(GamePiece(5))

    # places down all the pieces on hte board
    def placeGamePieces(self):
        for piece in self.player1Pieces:
            placed = False
            startX = 0
            startY = 0
            orientation = -3
            while not placed:
                placed = True
                orientation = self.randInt(0, 1)  # 0 represents down, 1 represents up
                startX = self.randInt(0, self.xDimen - 1)
                startY = self.randInt(0, self.yDimen - 1)
                if orientation == 0:
                    if self.checkInGameBoard(startX, startY + piece.returnLength() - 1):
                        for i in range(startY, startY + piece.returnLength()):
                            if self.player1Defense[startX][i] != 0:
                                placed = False
                    else:
                        placed=False

                if orientation == 1:
                    if self.checkInGameBoard(startX + piece.returnLength() - 1, startY):
                        for i in range(startX, startX + piece.returnLength()):
                            if not self.player1Defense[i][startY] == 0:
                                placed = False
                    else:
                        placed=False

            piece.setCoordinates(startX, startY, orientation, self.player1Defense)

        for piece in self.player2Pieces:
            placed = False
            startX = 0
            startY = 0
            orientation = -3
            while not placed:
                placed = True
                orientation = self.randInt(0, 1)  # 0 represents down, 1 represents up
                startX = self.randInt(0, self.xDimen - 1)
                startY = self.randInt(0, self.yDimen - 1)
                if orientation == 0:
                    if self.checkInGameBoard(startX, startY + piece.returnLength() - 1):
                        for i in range(startY, startY + piece.returnLength()):
                            if self.player2Defense[startX][i] != 0:
                                placed = False
                    else:
                        placed=False

                if orientation == 1:
                    if self.checkInGameBoard(startX + piece.returnLength() - 1, startY):
                        for i in range(startX, startX + piece.returnLength()):
                            if not self.player2Defense[i][startY] == 0:
                                placed = False
                    else:
                        placed=False

            piece.setCoordinates(startX, startY, orientation, self.player2Defense)

    # checks if a given location is inside the board or not
    def checkInGameBoard(self, i, j):
        return i < self.xDimen and j < self.yDimen

    def randInt(self, lower, upper):
        return random.randint(lower, upper)


# stores all trials with given players and cards
class Simulation:
    def __init__(self):
        self.trials = 100


def main():
    test = OneTrialSimulation(10, 10, 2, 2, 2, 2, 2)
    test.createBoards()
    test.createGamePieces()
    test.placeGamePieces()
    pprint.pprint(test.player1Defense)
    pprint.pprint(test.player2Defense)


main()
