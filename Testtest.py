class Person:
    
    def __init__(self, age, name): #initializer
        self.age = age
        self.name = name
  
    def __hash__(self): #hash method 
        return hash((self.age,self.name))
    
    
person = Person(23,'Matt') #our example person he uses the class Person

print('Class method hash. ',person.__hash__()) #call using class hash method
print('Hash Function: {}'.format(hash(person))) #call using hash function.