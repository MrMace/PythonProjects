class Queue:
    
    def __init__(self):
        self.items = []
        
    def emptyQ(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
        
    def dequeue(self):
        self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def printqueue(self):
        for items in self.items:
            print(items)
            
myQ = Queue()
print(myQ.emptyQ())
myQ.enqueue("Im first in")
myQ.enqueue("Second in line")
myQ.enqueue("Im Last")
myQ.printqueue()
myQ.dequeue()
myQ.printqueue()