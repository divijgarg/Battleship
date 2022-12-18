class GamePiece:

    def __init__(self, numPlaces):
        self.coordinates = []
        self.attackedCoordinates = []
        self.orientation = -2  # 0 is right, 1 is down
        self.destroyed = False
        self.numPlacesOccupied = numPlaces
        self.firstTimeDestroyed=False
    def returnLength(self):
        return self.numPlacesOccupied

        # stores the coordinates that the ship will occupy

    def setCoordinates(self, startingX, startingY, orient):
        # print(startingX, startingY)
        orientation = orient
        if orient == 0:
            for i in range(0, self.numPlacesOccupied):
                self.coordinates.append([startingX, startingY + i])
                # gameBoard[startingX][startingY + i] = self.numPlacesOccupied
        else:
            for i in range(0, self.numPlacesOccupied):
                self.coordinates.append([startingX + i, startingY])
                # gameBoard[startingX + i][startingY] = self.numPlacesOccupied

        # sets a position as destroyed

    def destroyCoord(self, i, j):
        self.attackedCoordinates.append([i, j])

    # checks if the ship is completely destroyed
    def checkIfDestroyed(self,player):
        if len(self.attackedCoordinates) == self.numPlacesOccupied:
            self.destroyed = True
            if not self.firstTimeDestroyed:
                player.orderOfDestruction.append(self.numPlacesOccupied)
                self.firstTimeDestroyed=True

    def checkInCoordinates(self, arr):
        for i in self.coordinates:
            if arr[0] == i[0] and arr[1] == i[1]:
                return True
        return False
