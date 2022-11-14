import random

from GamePiece import GamePiece

class OneTrialSimulation:

    def __init__(self,xD, yD, numD, numC, numS, numB, numCa):
        self.yDimen = yD
        self.xDimen = xD
        self.player1Defense=[]
        self.player1Attack=[]
        self.player2Defense=[]
        self.player2Attack=[]
        self.numDestroyer = numD
        self.player1Pieces=[]
        self.player2Pieces=[]
        self.numCruiser = numC
        self.numCarrier = numCa
        self.numBattleship = numB
        self.numSubmarine = numS

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
                        placed = False

                if orientation == 1:
                    if self.checkInGameBoard(startX + piece.returnLength() - 1, startY):
                        for i in range(startX, startX + piece.returnLength()):
                            if not self.player1Defense[i][startY] == 0:
                                placed = False
                    else:
                        placed = False

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
                        placed = False

                if orientation == 1:
                    if self.checkInGameBoard(startX + piece.returnLength() - 1, startY):
                        for i in range(startX, startX + piece.returnLength()):
                            if not self.player2Defense[i][startY] == 0:
                                placed = False
                    else:
                        placed = False

            piece.setCoordinates(startX, startY, orientation, self.player2Defense)

    # checks if a given location is inside the board or not
    def checkInGameBoard(self,i, j):
        return i < self.xDimen and j < self.yDimen

    def randInt(self, lower, upper):
        return random.randint(lower, upper)
