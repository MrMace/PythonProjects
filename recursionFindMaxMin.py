


current = 0
high = 0
low = 0
numList = [133,22,322,421,5,-6,7,8,9,10,29,11,12,13,14,15]   


def findMaxMin(numList,current,high,low):
    #base case return  if we reach end. 
    if current == len(numList):
        print("High number: {} ".format(high))
        print("Low number: {} ".format(low))
        return numList[0]
    '''Runs and checks the numList if it is higher than the current highest number
If it is higher than current high number then would assign to high var.
It also checks if the current number is the lowest number if it is sets the current num
to low. '''
    if numList[current] > high:
        high = numList[current]
    if numList[current]< low or low == 0:
        low = numList[current]
            
    #recursive calls itself and moves up the list until hits end of list.     
    return findMaxMin(numList, current + 1, high, low)
            
findMaxMin(numList,current, high,low)