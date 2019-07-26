class Stack:
    
    #Constructor creates a list 
    def __init__(self):
        self.stack = list()
        
    #Adding elements to stack
    def push(self,data):
        #Check to avoid duplicate entries
        if data not in self.stack:
            self.stack.append(data)
            return True
        return False
    
    #Remove last element from stack
    def pop(self):
        if len(self.stack) <=0:
            return("Stack Empty!")
    
        return self.stack.pop()

    #Getting the size of the stack
    def size(self):
        return len(self.stack)
    
    #Displays list
    def viewList(self):
        return self.stack
    
myStack = Stack() #node for class store. 
amtNumToPush = int(input("How many things would you like to push? ")) #gets the amount for list

#loops through to collect the users list items. 
for i in range(amtNumToPush):
    toPush = input("What do you want to push for the position {} in the list? ".format(i + 1)) #gets the input 
    myStack.push(toPush)#pushes the input
    
print(myStack.viewList()) #prints the list
