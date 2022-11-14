
class GamePiece:

    def __init__(self,numPlaces):
        self.coordinates = []
        self.attackedCoordinates = []
        self.orientation = -2  # 0 is down, 1 is right
        self.destroyed = False
        self.numPlacesOccupied = numPlaces



    def returnLength(self):
        return self.numPlacesOccupied

        # stores the coordinates that the ship will occupy


    def setCoordinates(self,startingX, startingY, orient, gameBoard):
        orientation = orient
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

        # sets a position as destroyed


    def destroyCoord(self,i, j):
        self.attackedCoordinates.append([i, j])

        # checks if the ship is completely destroyed


    def checkIfDestroyed(self):
        if len(self.attackedCoordinates) == len(self.numPlacesOccupied):
            destroyed = True
