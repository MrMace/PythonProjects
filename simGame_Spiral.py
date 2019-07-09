from random import random

def simGame_spiral():
    scoreA = 0
    scoreB = 0
    server = 'A'
    
    r = random()
    for i in range(30):
        
        if server == 'A':
            if r < .6:
                scoreA = scoreA + 1
            else:
                server = 'B'
                
        else: #B is serving
            if r < .4:
                scoreB = scoreB + 1
            else:
                server = 'A'
            
        print(server, scoreA, scoreB)