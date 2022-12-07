import random

from GamePiece import GamePiece
from Player import Player
import pprint
import time
from matplotlib import pyplot


class OneTrialSimulationNew:

    def __init__(self, xD, yD, numD, numC, numS, numB, numCa):
        self.yDimen = yD
        self.xDimen = xD
        self.player1 = Player()
        self.player2 = Player()
        self.numDestroyer = numD
        self.numCruiser = numC
        self.numCarrier = numCa
        self.numBattleship = numB
        self.numSubmarine = numS
        self.graphDrawn = False

    # creates the 10 x 10 game board for the game
    def createBoards(self):
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player1.defenseArray.append(arr)
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player1.attackArray.append(arr)
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player2.defenseArray.append(arr)
        for i in range(0, self.xDimen):
            arr = []
            for j in range(0, self.yDimen):
                arr.append(0)
            self.player2.attackArray.append(arr)

    # creates objects to represent all the game pieces
    def createGamePieces(self):
        for i in range(0, self.numDestroyer):
            self.player1.pieces.append(GamePiece(2))
            self.player2.pieces.append(GamePiece(2))
        for i in range(0, self.numCruiser):
            self.player1.pieces.append(GamePiece(3))
            self.player2.pieces.append(GamePiece(3))
        for i in range(0, self.numSubmarine):
            self.player1.pieces.append(GamePiece(3))
            self.player2.pieces.append(GamePiece(3))
        for i in range(0, self.numBattleship):
            self.player1.pieces.append(GamePiece(4))
            self.player2.pieces.append(GamePiece(4))
        for i in range(0, self.numCarrier):
            self.player1.pieces.append(GamePiece(5))
            self.player2.pieces.append(GamePiece(5))

    def trialCases(self):
        for i in range(0,len(self.player2.pieces)):
            piece=self.player2.pieces[i]
            piece.setCoordinates(i, 0, 0)
            for x in piece.coordinates:
                self.player2.defenseArray[x[0]][x[1]] = piece
    # places down all the pieces on hte board
    def placeGamePieces(self):
        for piece in self.player1.pieces:
            placed = False
            startX = 0
            startY = 0
            orientation = -3
            while not placed:
                print(79)
                placed = True
                orientation = self.randInt(0, 1)  # 0 represents down, 1 represents up
                startX = self.randInt(0, self.xDimen - 1)
                startY = self.randInt(0, self.yDimen - 1)
                if orientation == 0:
                    if self.checkInGameBoard(startX, startY + piece.returnLength() - 1):
                        for i in range(startY, startY + piece.returnLength()):
                            if self.player1.defenseArray[startX][i] != 0:
                                placed = False
                    else:
                        placed = False

                if orientation == 1:
                    if self.checkInGameBoard(startX + piece.returnLength() - 1, startY):
                        for i in range(startX, startX + piece.returnLength()):
                            if not self.player1.defenseArray[i][startY] == 0:
                                placed = False
                    else:
                        placed = False

            piece.setCoordinates(startX, startY, orientation)

            for x in piece.coordinates:
                self.player1.defenseArray[x[0]][x[1]] = piece

        for piece in self.player2.pieces:
            placed = False
            startX = 0
            startY = 0
            orientation = -3
            while not placed:
                print(111)
                placed = True
                orientation = self.randInt(0, 1)  # 0 represents down, 1 represents up
                startX = self.randInt(0, self.xDimen - 1)
                startY = self.randInt(0, self.yDimen - 1)
                if orientation == 0:
                    if self.checkInGameBoard(startX, startY + piece.returnLength() - 1):
                        for i in range(startY, startY + piece.returnLength()):
                            if self.player2.defenseArray[startX][i] != 0:
                                placed = False
                    else:
                        placed = False

                if orientation == 1:
                    if self.checkInGameBoard(startX + piece.returnLength() - 1, startY):
                        for i in range(startX, startX + piece.returnLength()):
                            if not self.player2.defenseArray[i][startY] == 0:
                                placed = False
                    else:
                        placed = False

            piece.setCoordinates(startX, startY, orientation)
            for x in piece.coordinates:
                self.player2.defenseArray[x[0]][x[1]] = piece
        # self.trialCases()

    # checks if a given location is inside the board or not
    def checkInGameBoard(self, i, j):
        return 0 <= i < self.xDimen and 0 <= j < self.yDimen

    # checks if a given spot is occupied or not
    def checkIfOccupied(self, i, j, arr):
        return arr[i][j] != 0

    def randInt(self, lower, upper):
        return random.randint(lower, upper)

    # bulk of code: represents the game algorithm. Does it for a general player.
    def doTurn(self, attackingPlayer, defendingPlayer):
        print("----------------------------------------------")
        print(attackingPlayer.currentTarget)
        pprint.pprint(attackingPlayer.attackArray)
        print(attackingPlayer.targetDirection)
        self.checkIfTargetsDestroyed(attackingPlayer, defendingPlayer)
        self.drawGraph(attackingPlayer, defendingPlayer)

        if len(attackingPlayer.currentTarget) == 0:
            self.doTurnRandomly(attackingPlayer, defendingPlayer)
        elif len(attackingPlayer.currentTarget[0]) == 1 and attackingPlayer.targetDirection == 0:
            self.doTurnButNoDirection(attackingPlayer, defendingPlayer)
        else:
            self.doTurnComplex(attackingPlayer, defendingPlayer)

    def doTurnRandomly(self, attackingPlayer, defendingPlayer):
        xChosen = self.randInt(0, self.xDimen - 1)
        yChosen = self.randInt(0, self.yDimen - 1)
        attackArray = attackingPlayer.attackArray
        defenseArray = defendingPlayer.defenseArray
        targets = attackingPlayer.currentTarget
        while attackArray[xChosen][yChosen] != 0:
            print(171)
            xChosen = self.randInt(0, self.xDimen - 1)
            yChosen = self.randInt(0, self.yDimen - 1)

        if defenseArray[xChosen][yChosen] == 0:  # space was empty--failed attack
            attackArray[xChosen][yChosen] = -1
        elif defenseArray[xChosen][yChosen].checkInCoordinates([xChosen, yChosen]):
            targets.append([[xChosen, yChosen, defenseArray[xChosen][yChosen].returnLength()]])
            attackingPlayer.targetLength = defenseArray[xChosen][yChosen].returnLength()
            self.destroyCoordinate(xChosen, yChosen, attackingPlayer, defendingPlayer)

    def doTurnComplex(self, attackingPlayer, defendingPlayer):
        self.shipsOverlapCase(attackingPlayer, defendingPlayer)
        attackArray = attackingPlayer.attackArray
        defenseArray = defendingPlayer.defenseArray
        targets = attackingPlayer.currentTarget
        direction = attackingPlayer.targetDirection
        attackedLength = len(targets[0])


        changes = self.returnXYBasedOnDirection(direction)
        xChange = changes[0]
        yChange = changes[1]

        if attackingPlayer.forwards:
            xChosen = targets[0][attackedLength - 1][0] + xChange
            yChosen = targets[0][attackedLength - 1][1] + yChange
        else:
            xChosen = targets[0][0][0] + xChange
            yChosen = targets[0][0][1] + yChange

        if not self.checkInGameBoard(xChosen, yChosen) or attackArray[xChosen][
            yChosen] != 0:  # ensures the user hasn't chosen a space they've attacked before
            # print("happened")
            # print(attackingPlayer.targetDirection)
            attackingPlayer.flipDirection()
            # print(attackingPlayer.targetDirection)
            attackingPlayer.setForwards()
            direction = attackingPlayer.targetDirection
            changes = self.returnXYBasedOnDirection(direction)
            xChange = changes[0]
            yChange = changes[1]
            # print([xChange, yChange])
            if attackingPlayer.forwards:
                xChosen = targets[0][attackedLength - 1][0] + xChange
                yChosen = targets[0][attackedLength - 1][1] + yChange
            else:
                xChosen = targets[0][0][0] + xChange
                yChosen = targets[0][0][1] + yChange

        # print([xChosen, yChosen])
        if defenseArray[xChosen][yChosen] == 0:
            attackArray[xChosen][yChosen] = -1

        elif defenseArray[xChosen][yChosen].returnLength() != attackingPlayer.targetLength:
            targets.append([[xChosen, yChosen, defenseArray[xChosen][yChosen].returnLength()]])
            self.destroyCoordinate(xChosen, yChosen, attackingPlayer, defendingPlayer)
            self.doTurn(attackingPlayer, defendingPlayer)
        else:
            attackingPlayer.addNewAttacked([xChosen, yChosen, defenseArray[xChosen][yChosen].returnLength()])
            self.destroyCoordinate(xChosen, yChosen, attackingPlayer, defendingPlayer)
            self.doTurn(attackingPlayer, defendingPlayer)

    def doTurnButNoDirection(self, attackingPlayer, defendingPlayer):
        attackArray = attackingPlayer.attackArray
        defendingArray = defendingPlayer.defenseArray
        targets = attackingPlayer.currentTarget
        xChosen = targets[0][0][0]
        yChosen = targets[0][0][1]

        direction = self.randInt(1, 4)
        changes = self.returnXYBasedOnDirection(direction)
        xChange = changes[0]
        yChange = changes[1]

        while not self.checkInGameBoard(xChosen + xChange, yChosen + yChange) or (
                attackArray[xChosen + xChange][yChosen + yChange] != 0):
            print(248)
            direction = self.randInt(1, 4)
            changes = self.returnXYBasedOnDirection(direction)
            xChange = changes[0]
            yChange = changes[1]

        xChosen = xChosen + xChange
        yChosen = yChosen + yChange

        if defendingArray[xChosen][yChosen] == 0:
            attackArray[xChosen][yChosen] = -1

        elif defendingArray[xChosen][yChosen].returnLength() != attackingPlayer.targetLength:
            targets.append([[xChosen, yChosen, defendingArray[xChosen][yChosen].returnLength()]])
            self.destroyCoordinate(xChosen, yChosen, attackingPlayer, defendingPlayer)
            self.doTurn(attackingPlayer, defendingPlayer)
        else:
            attackingPlayer.targetDirection = direction
            attackingPlayer.setForwards()  # sets the forward direction since now we know, will use this for future attacks
            attackingPlayer.addNewAttacked([xChosen, yChosen, defendingArray[xChosen][yChosen].returnLength()])
            self.destroyCoordinate(xChosen, yChosen, attackingPlayer, defendingPlayer)
            self.doTurn(attackingPlayer, defendingPlayer)

    def shipsOverlapCase(self, attackingPlayer, defendingPlayer):
        attackArray = attackingPlayer.attackArray
        defenseArray = defendingPlayer.defenseArray
        targets = attackingPlayer.currentTarget
        direction = attackingPlayer.targetDirection
        attackedLength = len(targets[0])

        changes = self.returnXYBasedOnDirection(direction)
        xChange = abs(changes[0])
        yChange = abs(changes[1])

        if attackedLength > 1:
            x=targets[0][attackedLength - 1][0] + xChange
            y=targets[0][attackedLength - 1][1] + yChange
            if not self.checkInGameBoard(x,y) or attackArray[x][y] != 0:
                x = targets[0][0][0] - xChange
                y = targets[0][0][1] - yChange
                if attackedLength==targets[0][0][2]:

                elif not self.checkInGameBoard(x,y) or attackArray[x][y] != 0:
                    print("HHHHHHHH")
                    print(targets)
                    tempArray = targets[0]
                    targets.pop(0)
                    for i in tempArray:
                        targets.insert(0, [i])
                    if direction == 1 or direction == 3:
                        attackingPlayer.targetDirection = 4
                    else:
                        attackingPlayer.targetDirection = 3
                    attackingPlayer.forwards=True
                    print(targets)


    def returnXYBasedOnDirection(self, direction):
        changes = [0, 0]
        if direction % 2 == 1:  # code to connect direction to change in coordinates
            changes[0] = direction - 2
        else:
            changes[1] = direction - 3

        return changes

    def destroyCoordinate(self, x, y, attackingPlayer, defendingPlayer):
        length = defendingPlayer.defenseArray[x][y].numPlacesOccupied
        defendingPlayer.defenseArray[x][y].destroyCoord(x, y)
        attackingPlayer.attackArray[x][y] = length

    def checkIfTargetsDestroyed(self, attackingPlayer, defendingPlayer):
        targets = attackingPlayer.currentTarget
        defenseArray = defendingPlayer.defenseArray
        attackArray = attackingPlayer.attackArray
        for i in defendingPlayer.pieces:
            i.checkIfDestroyed()

        changed = False
        while len(targets) > 0 and defenseArray[targets[0][0][0]][targets[0][0][1]].destroyed:
            print(325)
            targets.pop(0)
            attackingPlayer.targetLength = 0
            attackingPlayer.targetDirection = 0
            changed = True
        if changed and len(targets) > 0:
            print("huhhh")
            attackingPlayer.targetLength = targets[0][0][2]
            if len(targets[0]) > 1:
                attackingPlayer.targetDirection = attackingPlayer.determineDirection()

    def checkIfGameOver(self):
        counter1 = 0
        counter2 = 0
        for i in self.player1.pieces:
            if i.destroyed: counter1 += 1
        if counter1 == len(self.player1.pieces): return True
        for i in self.player2.pieces:
            if i.destroyed: counter2 += 1
        if counter2 == len(self.player2.pieces): return True
        return False

    def drawGraph(self, player1, player2):

        # show the image
        #    plt.figure(figsize=(5, 5))
        pyplot.clf()
        pyplot.imshow(player1.attackArray, cmap='hot', interpolation='nearest')

        pyplot.colorbar()
        # print("Pausing...")
        pyplot.pause(0.001)
