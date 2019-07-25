class Queue:
    DEFUALT_CAPACITY = 10
    
    def __init__(self):
        #Creates empty queue
        self._data = [] * Queue.DEFAULT_CAPACITY
        self.size = 0
        self.foq = 0 #front of queue
        
        #Returns num of elements in the queue
        def __len__(self):
            return self.size
        
        #Return if Queue is empty
        def emptyQ(self):
            return self.size
        
        #Returns but dosnt remove front of Q If empty raise exception
        def first(self):        
            if self.emptyQ():
                raise Empty("The Queue is empty")
            return self._data[self.foq]
        
        def dequeue(self):
            if self.emptyQ():
                raise Empty("The Queue is empty")
            answer = self._data[self.foq]
            self._data[self.foq] = None
            self.foq = (self.foq + 1) % len(self._data)
            self.size -= 1
            return answer
        
        #add element to back of Q
        def enqueue(self, element):
            if self.size == len(self._data):
                self.resize(2 * len(self._data))
            available = (self.foq + self.size) % len(self._data)
            self._data[available] = element
            self.size +=1
            
            #resize new list
        def resize(self, capacity):
            old = self._data
            self._data = [None] * capacity
            walk = self.foq
            for k in range(self.size):
                walk = (1 + walk) % len(old)
                self.foq = 0
                
myQ = Queue()
myQ.enqueue(5)
myQ.enqueue(3)
len(myQ)



        
        