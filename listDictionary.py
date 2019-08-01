#What is the difference between a list and a dictionary?
#A LIST is a python data type that represents sequential collections. List can grow and shrink as needed.
#Items of a list are accessed through subscriting.
#A DICTIONARY is an unordered python collection that allows its values be associated with keys. 
#How are they coded differently and what different implementations they have?
#Build a script that utilizes at least one list and one dictionary.

theList = ["dog", "cat", "monkey", "snake", "dragon"]
theDictionary = {"dog":'brown', "cat":'orange', "monkey":'brown',"snake":'black',"dragon":'red'}
def listExample(theList):
    print("Your list: " , theList)
    
def dictionaryExample(theDictionary):
    print("Your dictionary: ",theDictionary)
    
def useBoth(theList,theDictionary):
    
    listlength = len(theList)
    for i in range(listlength):
        animal = theList[i],theDictionary[theList[i]]
        print(animal)
        print(hash(animal))
        
        
def main():
    
    userInput = input("Which do you want to use input L for list or D for Dictionary: ")
    
    if userInput == 'L' or userInput == 'l':
        
        listExample(theList)
            
    elif userInput == 'D' or userInput == 'd':
    
        dictionaryExample(theDictionary)
    elif userInput == '':
        useBoth(theList,theDictionary)
    else:
        print("You must enter either L or D. Try again!")
        main()
main()