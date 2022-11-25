class Player:
    def __init__(self):
        self.defenseArray = []
        self.attackArray = []
        self.pieces = []
        self.currentTarget = []
        self.targetLength = 0
        self.targetDirection = 0  # 1=left, 2=down, 3=right, 4= up
        self.forwards = False  # left to right, up to down

    def setForwards(self):
        if self.targetDirection == 1 or self.targetDirection == 4:
            self.forwards = False
        else:
            self.forwards = True

    def addNewAttacked(self,arr):
        if self.forwards:
            self.currentTarget.insert(0,arr)
        else:
            self.currentTarget.append(arr)

    def flipDirection(self):
        if self.targetDirection==1 or self.targetDirection==2:
            self.targetDirection+=2
        else:
            self.targetDirection-=2
