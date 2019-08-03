#What is the difference between a list and a dictionary?
#Dictionaries is a hash table implementation it uses key value stores and it is not ordered. Where a list is ordered
#and instead of using key values stores the values are indexed.

#How are they coded differently and what different implementations they have?
#With list you have to enclose it with []. With a dictionary it is enclosed with {}.
#Items removed using almost the same syntax del list[index].Items removed using del dictionary[key].



#Build a script that utilizes at least one list and one dictionary.
'''
This program uses a list to search a dictionary.
'''
theList = ["dog", "cat", "monkey", "snake", "dragon", "mouse"]  #The List
#The Dictionary
theDictionary = {"dog":'brown', "cat":'orange', "mouse":"grey","monkey":'brown',"snake":'black',"dragon":'red'} 

def listExample(theList): #Print list function.
    print("Your list: " , theList)
    
def dictionaryExample(theDictionary): #print Dictionary function.
    print("Your dictionary: ",theDictionary)
    
def useBoth(theList,theDictionary): #uses both the list and dictionary together. 
    
    listlength = len(theList) #gets the length of the list
    for i in range(listlength): #loops through the list using the length of it
        if theList[i] in theDictionary: #if the current list item matches Print to console the color of it
            print('Match for {}!'.format(theList[i]))
            print('Its color is {}!'.format(theDictionary[theList[i]]))
        else: #if no match is found
            print('No Match for {}!'.format(theList[i]))
            
def main():
    #gets user input for what to do
    print("Which do you want to see? Enter L for list or D for Dictionary.Or just press enter ")
    userInput = input("to use the list to search the dictionary:   ")
    
    #Depending on what is entered call specific function.
    if userInput == 'L' or userInput == 'l':     #if uppercase or lowercase L is entered Display List.
        listExample(theList)         
    elif userInput == 'D' or userInput == 'd':#if uppercase or lowercase D is entered Display Dictionary
        dictionaryExample(theDictionary)
    elif userInput == '': #if nothing is entered Use list to search dictionary. 
        useBoth(theList,theDictionary)
    else: #if anthing other than '', L,l,D,or d are entered rerun.
        print("You must enter either L , D , or press enter. Try again!")
        main()
main() #calls the main function. 