from random import random

def printWelcomeMessage():
    print("This program simulates a game of racquetball between two")
    print("players called 'A' and 'B'. The abilities of each player is ")
    print("indicated by a probability (a number between 0 and 1) that ")
    print("the player wins the point when serving. Player A always")
    print("has the frist serve")

def getInputValues():
    probA = float(input("Enter the probability of player A scoring on thier serve: "))
    probB = float(input("Enter the probability of player B scoring on their serve: "))
    numOfSim = int(input("Enter the number of games to simulate: "))
    return probA, probB, numOfSim

def printResults(winsA, winsB):
    totalGames = winsA + winsB
    print("Player A wins: {0} {1:0.1f}% ".format(winsA, 100 * winsA/totalGames))
    print("Player B wins: {0} {1:0.1f}% ".format(winsB, 100 * winsB/totalGames))
    
def simNGames(numOfSim, probA, probB):
    winsA = 0
    winsB = 0
    for gameNum in range (numOfSim):
        scoreA, scoreB = simGame(probA, probB)
        if scoreA == 15:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
            
    return winsA, winsB
    
def simGame(probA,probB):
    scoreA = 0
    scoreB = 0
    server = 'A'
    
    while not gameOver(scoreA, scoreB):
        if server == 'A':
            if random() < probA:
                scoreA = scoreA + 1
            else: server = 'B'
        else: #b is serving
            if random() < probB:
                scoreB = scoreB + 1
            else:
                server = 'A'
    
    return scoreA, scoreB
    
def gameOver(scoreA, scoreB):
    return scoreA == 15 or scoreB == 15


def main():
    printWelcomeMessage()
    probA, probB, numOfSim = getInputValues()
    winsA, winsB = simNGames(numOfSim, probA, probB)
    printResults(winsA, winsB)
    

main()

        