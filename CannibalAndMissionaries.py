

"""
Three missionaries and three cannibals come to a river and find a boat that holds two people. 
Everyone must get across the river to continue on the journey. However, if the cannibals ever 
outnumber the missionaries on either bank, the missionaries will be eaten. Find a series of 
crossings that will get everyone safely to the other side of the river.
"""

# initial configuration That has 3 missionaries and 3 cannibals on left side of the river. 
leftSideRiver = {'cannibals': 3, 'missionaries': 3}
boat = {'cannibals': 0, 'missionaries': 0}
rightSideRiver = {'cannibals': 0, 'missionaries': 0}

def print_state(dct1, dct2, dct3):
   
    msg = """
    Left Side of the river: {} cannibal(s), {} missionary/ies
    On the Boat: {} cannibal(s), {} missionary/ies
    Right side of the river: {} cannibal(s), {} missionary/ies
    """

    print(msg.format(dct1['cannibals'], dct1['missionaries'], dct2['cannibals'], dct2['missionaries'],
                     dct3['cannibals'], dct3['missionaries']))

def cannibalsAndMissionaries(r1=leftSideRiver, bo=boat,r2=rightSideRiver):
    if all(x == 0 for x in r2.values()):  # right Side River is empty
        print_state(r1, bo, r2)
        r1['cannibals'] -= 1  # 1 cannibal leaves leftSideRiver and ...
        bo['cannibals'] += 1  # ... goes on board

    r1['missionaries'] -= 1  # 1 missionary leaves leftSideRiver and ...
    bo['missionaries'] += 1  # ... goes on board
    print_state(r1, bo, r2)

    if all(x == 0 for x in r1.values()):  # leftSideRiver is empty
        bo['cannibals'], bo['missionaries'] = 0, 0  # 1 cannibal and 1 missionary go out on the boat
        r2['cannibals'] += 1  # 1 cannibal steps out on rightSideRiver
        r2['missionaries'] += 1  # 1 missionary steps out on rightSideRiver
        print_state(r1, bo, r2)
        return  # when the final condition is met
    
    #1 missionary gets out of the boat and steps to the right side of river. 
    bo['missionaries'] -= 1  # missionary goes out of boat
    r2['missionaries'] += 1  # steps out on rightSideRiver.
    print_state(r1, bo, r2)

    #1 cannibal leaves left side of the river and gets on boat. 
    r1['cannibals'] -= 1  # 1 cannibal leaves leftSideRiver.
    bo['cannibals'] += 1  # gets on the boat.
    print_state(r1, bo, r2)

    #1 cannibal gets out of the boat and steps to the right side of river. 
    bo['cannibals'] -= 1  # 1 cannibal gets out of the boat.
    r2['cannibals'] += 1  # steps out on right side of the river.
    print_state(r1, bo, r2)

    cannibalsAndMissionaries(r1, bo, r2)  # recursivly calls its self. 


def main():
    cannibalsAndMissionaries()
main()
