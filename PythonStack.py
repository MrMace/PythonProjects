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
    
myStack = Stack()
print(myStack.push(5))
print(myStack.push(6))
print(myStack.push(9))
print(myStack.push(5)) #false
print(myStack.size())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.size())
print(myStack.pop())