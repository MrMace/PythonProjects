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

dQ.addFront("FrontOne")
dQ.addFront("SecondFront")
dQ.addBack("Added Back")
dQ.addBack("Second Back")
print(dQ.size())
print(dQ.viewList())
print(dQ.isEmpty())
dQ.addFront("Added")
print(dQ.viewList())
