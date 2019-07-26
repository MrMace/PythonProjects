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
amtNumToPush = int(input("How many things would you like to push? ")) #gets the amount for list

#loops through to collect the users list items. 
for i in range(amtNumToPush):
    toPush = input("What do you want to push for the position {} in the list? ".format(i + 1)) #gets the input 
    myQ.enqueue(toPush)#pushes the input
    
print(myQ.viewList()) #prints the list
