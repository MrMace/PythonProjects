#Dictionaries is a hash table implementation it uses key value stores and it is not ordered. Where a list is ordered
#and instead of using key values stores the values are indexed.
#With list you have to enclose it with []. With a dictionary it is enclosed with {}.
#Items can be removed using almost the same syntax operator del list[index] for the list and del dictionary[key].
#According to our text books graphs List have 10 different methods where Dictionaries have half that of 5.

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