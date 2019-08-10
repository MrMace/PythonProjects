import random

class BinaryHeap:
    def __init__(self):#Our constructor 
        self.heapList = [0]
        self.currentSize = 0
        
#Percolates the new node up to its proper position.
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            
#Adds an item to the list, using append.
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
        
    #Percolates the new node down to its proper position. Swap the root with smallest child less than root.
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i) 
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
 #method that works with the percDown. which is swapped until node
    # is swapped into a position. where it is less than both children. 
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
            
   #deletes the minimum item from the binary heap         
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    
#build the new heap from a list of items.
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]      
        while (i > 0):
            self.percDown(i)
            i = i - 1

#uses the buildHeap method 
def BuildHSort(list):
    bh = BinaryHeap()
    bh.buildHeap(list)
    sortedList = []
    i = 0
    while i < len(list):
        sortedList.append(bh.delMin())
        print(sortedList)
        i = i + 1
    return print(sortedList)         

 #Creates a random list of numbers to use in program. 
def randomListNum():
    randoList = random.sample(range(1,100), 10)
    return randoList
randomList = randomListNum()

def usingInsert(randomList):
    myListLen = len(randomList) #gets length of list
    bh = BinaryHeap() #simplifies class calling
    loopNum = myListLen #for loop initialization
    #Shows the binary tree results from inserting intergers one at a time.
    print(randomList) #prints my list for first half
    
    for i in range(myListLen):
        bh.insert(randomList[i])
    newList = [] #var for new list
    
    while loopNum  != 0 : 
        insertNum = bh.delMin() #Gets the new number(min value) from the bh.
        newList.append(insertNum)   #insert new number in the list
        print(newList) #print current number
        loopNum = loopNum - 1 #used for loop  



usingInsert(randomList)
print("___________________Question 2___________________________")
BuildHSort(randomList)
