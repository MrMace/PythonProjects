class Deque:
    
    #Constructor
    def __init__(self):
        self.items = []
        
    #Checks if empty  
    def isEmpty(self):
        return self.items == []
    
    #adds to the front
    def addFront(self, item):
        self.items.append(item)
        
     #adds to back   
    def addBack(self, item):
        self.items.insert(0,item)
        
     #removes from front   
    def removeFront(self):
        return self.items.pop()
    
    #removes from back
    def removeBack(self):
        return self.items.pop(0)
    
    #returns size
    def size(self):
        return len(self.items)
    
    #returns list contents
    def viewList(self):
        return self.items
    
    
dQ = Deque()

amtNumToPush = int(input("How many things would you like to push? ")) #gets the amount for list

#loops through to collect the users list items. 
for i in range(amtNumToPush):
    toPush = input("What do you want to push for the position {} in the list? ".format(i + 1)) #gets the input 
    dQ.addFront(toPush)#pushes the input
    
print(dQ.viewList()) #prints the list


