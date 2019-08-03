class Person:
    def __init__(self, age, name): #initializer
        self.age = age
        self.name = name

    def __eq__(self, other): #eq function. Don't have to define it is defined for all objects.
        return self.age == other.age and self.name == other.name

    def __hash__(self): #has function
        return hash((self.age, self.name))

person = Person(23, 'Matt')
print("Class function: " ,person.__hash__()) #calls the funtion.
print("The hash is: {} ".format(hash(person))) #uses interanal function instead of the class hash