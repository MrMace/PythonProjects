class Queue:
    
    #construct the list
    def __init__(self):
        self.items = []
        
     #check if empty   
    def emptyQ(self):
        return self.items == []
    
    #insert into queue
    def enqueue(self,item):
        self.items.insert(0,item)
        
     #remove from queue   
    def dequeue(self):
        self.items.pop()
        
    # returns size of list   
    def size(self):
        return len(self.items)
    
    #prints out each item
    def printqueue(self):
        for items in self.items:
            print(items)
    
    #prints out list
    def viewList(self):
        return self.items
            
myQ = Queue()
print(myQ.emptyQ())
myQ.enqueue("Im first in")
myQ.enqueue("Second in line")
myQ.enqueue("Im Last")
myQ.printqueue()
myQ.dequeue()
myQ.printqueue()
print(myQ.emptyQ())
print(myQ.viewList())
