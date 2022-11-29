import random

from GamePiece import GamePiece
from Player import Player
import pprint


class OneTrialSimulation:

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

    # places down all the pieces on hte board
    def placeGamePieces(self):
        for piece in self.player1.pieces:
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

    # checks if a given location is inside the board or not
    def checkInGameBoard(self, i, j):
        return 0<=i < self.xDimen and 0<=j < self.yDimen

    # checks if a given spot is occupied or not
    def checkIfOccupied(self, i, j, arr):
        return arr[i][j] != 0

    def randInt(self, lower, upper):
        return random.randint(lower, upper)

    # bulk of code: represents the game algorithm. Does it for a general player.
    def doTurn(self, attackingPlayer, defendingPlayer):
        pprint.pprint(attackingPlayer.attackArray)
        print("direction: ", attackingPlayer.targetDirection)
        print(attackingPlayer.currentTarget)
        print(attackingPlayer.forwards)
        #this code checks if the current target for the player has been completely destroyed.
        if attackingPlayer.targetLength > 0:
            if attackingPlayer.targetLength == len(attackingPlayer.currentTarget[0]):
                attackingPlayer.currentTarget.pop(0) #removes the target since destroyed
                attackingPlayer.direction = 0
                if len(attackingPlayer.currentTarget) > 0: # if there is another target the program identified, it focuses on that now
                    attackingPlayer.targetLength = attackingPlayer.attackArray[attackingPlayer.currentTarget[0][0][0]][
                        attackingPlayer.currentTarget[0][0][1]]
                else:
                    attackingPlayer.targetLength = 0
        # code to find a new target
        if len(attackingPlayer.currentTarget) == 0:
            xChosen = self.randInt(0, self.xDimen - 1)
            yChosen = self.randInt(0, self.yDimen - 1)
            while attackingPlayer.attackArray[xChosen][yChosen] != 0:  # ensures the user hasn't chosen a space they've attacked before
                xChosen = self.randInt(0, self.xDimen - 1)
                yChosen = self.randInt(0, self.yDimen - 1)
            if defendingPlayer.defenseArray[xChosen][yChosen] == 0: #space was empty--failed attack
                attackingPlayer.attackArray[xChosen][yChosen] = -1
            else:
                attackingPlayer.attackArray[xChosen][yChosen] = defendingPlayer.defenseArray[xChosen][
                    yChosen].numPlacesOccupied #sets the space as destroyed on attacker's end
                attackingPlayer.currentTarget.append([]) #adds a new target to the list
                attackingPlayer.currentTarget[0].append([xChosen, yChosen]) #adds that point to the current target
                attackingPlayer.targetLength = defendingPlayer.defenseArray[xChosen][yChosen].numPlacesOccupied #sets the goal length of the target
                defendingPlayer.defenseArray[xChosen][yChosen].destroyCoord(xChosen, yChosen) #destroys the spot on the defending player's end
                self.doTurn(attackingPlayer, defendingPlayer) #player gets another turn
        # code to attack a probable target
        else:
            # if it's the first time a target detected, then we need to find a direction to go in. Hence, this finds that direction
            if len(attackingPlayer.currentTarget[0]) == 1:
                xChosen = attackingPlayer.currentTarget[0][0][0]
                yChosen = attackingPlayer.currentTarget[0][0][1]
                direction = self.randInt(1, 4)
                xChange = 0
                yChange = 0
                if direction % 2 == 1: #code to connect direction to change in coordinates
                    xChange = direction - 2
                else:
                    yChange = direction - 3
                while not self.checkInGameBoard(xChosen + xChange, yChosen + yChange) \
                        or attackingPlayer.attackArray[xChosen + xChange][yChosen + yChange] != 0:  # ensures the user hasn't chosen a space they've attacked before
                    direction = self.randInt(1, 4)
                    xChange = 0
                    yChange = 0
                    if direction % 2 == 1:
                        xChange = direction - 2
                    else:
                        yChange = direction - 3
                xChosen = xChosen + xChange
                yChosen = yChosen + yChange

                if defendingPlayer.defenseArray[xChosen][yChosen] == 0: #failed attack
                    attackingPlayer.attackArray[xChosen][yChosen] = -1
                elif defendingPlayer.defenseArray[xChosen][
                    yChosen].returnLength() != attackingPlayer.targetLength or not \
                defendingPlayer.defenseArray[attackingPlayer.currentTarget[0][0][0]][attackingPlayer.currentTarget[0][0][1]].checkInCoordinates([xChosen, yChosen]): #checks to make sure that the attacked spot is a part of the current target ship.
                    attackingPlayer.currentTarget.append([[xChosen, yChosen]]) #creates a new target for the program to return to once the current target is eliminated
                    attackingPlayer.attackArray[xChosen][yChosen] = defendingPlayer.defenseArray[xChosen][
                        yChosen].numPlacesOccupied #sets that position as attacked
                    # attackingPlayer.addNewAttacked([xChosen, yChosen])
                    defendingPlayer.defenseArray[xChosen][yChosen].destroyCoord(xChosen, yChosen) #destroys coordinate on the defenders end
                    self.doTurn(attackingPlayer, defendingPlayer) #redo turn

                else:
                    attackingPlayer.attackArray[xChosen][yChosen] = defendingPlayer.defenseArray[xChosen][
                        yChosen].numPlacesOccupied
                    attackingPlayer.targetDirection = direction
                    attackingPlayer.setForwards() #sets the forward direction since now we know, will use this for future attacks
                    attackingPlayer.addNewAttacked([xChosen, yChosen])
                    defendingPlayer.defenseArray[xChosen][yChosen].destroyCoord(xChosen, yChosen)
                    self.doTurn(attackingPlayer, defendingPlayer)
            # code to continue attacking target, pretty much same as before code, but direction is fixed unless a previously hit spot is found
            else:
                direction = attackingPlayer.targetDirection
                attackedLength = len(attackingPlayer.currentTarget[0])
                xChange = 0
                yChange = 0
                if direction % 2 == 1:
                    xChange = direction - 2
                else:
                    yChange = direction - 3

                if attackingPlayer.forwards:
                    xChosen = attackingPlayer.currentTarget[0][attackedLength - 1][0] + xChange
                    yChosen = attackingPlayer.currentTarget[0][attackedLength - 1][1] + yChange
                else:
                    xChosen = attackingPlayer.currentTarget[0][0][0] + xChange
                    yChosen = attackingPlayer.currentTarget[0][0][1] + yChange

                if not self.checkInGameBoard(xChosen, yChosen) or \
                        attackingPlayer.attackArray[xChosen][
                            yChosen] != 0:  # ensures the user hasn't chosen a space they've attacked before
                    print(attackingPlayer.targetDirection)
                    attackingPlayer.flipDirection()
                    print("direction flipped")
                    print(attackingPlayer.targetDirection)
                    attackingPlayer.setForwards()
                    direction = attackingPlayer.targetDirection
                    xChange = 0
                    yChange = 0
                    if direction % 2 == 1:
                        xChange = direction - 2
                    else:
                        yChange = direction - 3

                    if attackingPlayer.forwards:
                        xChosen = attackingPlayer.currentTarget[0][attackedLength - 1][0] + xChange
                        yChosen = attackingPlayer.currentTarget[0][attackedLength - 1][1] + yChange
                    else:
                        xChosen = attackingPlayer.currentTarget[0][0][0] + xChange
                        yChosen = attackingPlayer.currentTarget[0][0][1] + yChange

                if defendingPlayer.defenseArray[xChosen][yChosen] == 0:
                    attackingPlayer.attackArray[xChosen][yChosen] = -1
                elif defendingPlayer.defenseArray[xChosen][
                    yChosen].returnLength() != attackingPlayer.targetLength or not \
                defendingPlayer.defenseArray[attackingPlayer.currentTarget[0][0][0]][attackingPlayer.currentTarget[0][0][1]].checkInCoordinates([xChosen, yChosen]):
                    attackingPlayer.currentTarget.append([[xChosen, yChosen]])
                    attackingPlayer.attackArray[xChosen][yChosen] = defendingPlayer.defenseArray[xChosen][
                        yChosen].numPlacesOccupied
                    # attackingPlayer.addNewAttacked([xChosen, yChosen])
                    defendingPlayer.defenseArray[xChosen][yChosen].destroyCoord(xChosen, yChosen)
                    self.doTurn(attackingPlayer, defendingPlayer)
                else:
                    attackingPlayer.attackArray[xChosen][yChosen] = defendingPlayer.defenseArray[xChosen][
                        yChosen].numPlacesOccupied
                    attackingPlayer.addNewAttacked([xChosen, yChosen])
                    defendingPlayer.defenseArray[xChosen][yChosen].destroyCoord(xChosen, yChosen)
                    self.doTurn(attackingPlayer, defendingPlayer)

        for i in defendingPlayer.pieces:
            i.checkIfDestroyed()
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
