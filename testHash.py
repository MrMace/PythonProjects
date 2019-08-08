class Person:
    
    def __init__(self, age, name):
        self.age
        self.name
        
    def __eq__(self,other):
        return self.age == other.age and self.name == other.name
    
    def __hash__(self):
        return((self.age,self.name))
    

person = Person(23, 'Matt')
print('Class hash ', person.__hash__())
print('The hash is: {}'.format(hash(person)))
        
    