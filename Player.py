import numpy as np
class Player:
    def __init__(self):
        self.defenseArray = []
        self.attackArray = []
        self.pieces = []
        self.currentTarget = []
        self.targetLength = 0
        self.targetDirection = 0  # 1=up, 2=left, 3=down, 4= right
        self.forwards = False  # left to right, up to down

    def setForwards(self):
        if self.targetDirection == 1 or self.targetDirection == 2:
            self.forwards = False
        else:
            self.forwards = True

    def addNewAttacked(self,arr):
        if self.forwards:
            self.currentTarget[0].append(arr)
        else:
            self.currentTarget[0].insert(0,arr)

    def flipDirection(self):
        if self.targetDirection==1 or self.targetDirection==2:
            self.targetDirection+=2
        else:
            self.targetDirection-=2

    def determineDirection(self):
        difference=np.subtract(self.currentTarget[0][0], self.currentTarget[0][1])
        if difference[0]==1:
            return 3
        return 4
