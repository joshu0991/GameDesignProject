import time
import random


class PlayerTimer:
    def __init__(self, difficulty, numberOfPlayers):
        self.timeLimit = self.setTimeLimit(difficulty)
        self.numberOfPlayer = numberOfPlayers
        self.playerList = []
        self.startTime = time.time()
        self.timer = 0
        self.initalizePlayers()

    def setTimeLimit(self, difficulty):
        timeLimit = 0
        if difficulty == 'easy':
            timeLimit = random.randint(50, 60)
        elif difficulty == 'medium':
            timeLimit = random.randint(35, 45)
        elif difficulty == 'hard':
            timeLimit = random.randint(20, 25)
        return timeLimit

    def initalizePlayers(self):
        x = 0
        while x <= self.numberOfPlayer:
            self.playerList.append(0)
            x = x + 1

    def takeInput(self, action, playerNumber):
        if action != 'stop':
            self.timer = time.time() - self.startTime
        else:
            self.startTime = time.time()
        self.checkTimer(playerNumber)

    def getTimer(self, playerNumber):
        return self.timer

    def storeTotalTime(self, playerNumber, totalTime):
        self.playerList[playerNumber - 1] = totalTime
        print ("totalTime" + str(self.playerList[playerNumber - 1]))
        
    def checkTimer(self, playerNumber):
        if self.playerList[playerNumber - 1] > self.timeLimit:
            self.startFan()
            
    def startFan(self):
        pass