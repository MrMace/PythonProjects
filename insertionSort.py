<<<<<<< HEAD
#List given 
givenList =  [1,2,3,5,4,6,7,8,9,10]

'''
This is the Insertion sorting algorithm 
'''

def insertionSort(givenList): #Function
    
    listLen = len(givenList) #gets length of the list
    
    for i in range(1, listLen): #goes through 1 and length of list
        
        key = givenList[i]
        
        
        #Move through list, anything greater than key is moved
        #ahead one position.
        j = i - 1
        
        while j >= 0 and key < givenList[j]:
            givenList[j + 1] = givenList[j]
            j -= 1
        givenList[j + 1] = key

insertionSort(givenList)

#prints out to our console the list. 
print("The sorted list is: {} ".format(givenList))
=======
#List given 
givenList =  [1,2,3,5,4,6,7,8,9,10]


'''
This is the Insertion sorting algorithm 
'''

def insertionSort(givenList): #Function
    
    listLen = len(givenList) #gets length of the list
    
    for i in range(1, listLen): #goes through 1 and length of list
        
        key = givenList[i]
        
        
        #Move through list, anything greater than key is moved
        #ahead one position.
        j = i - 1
        
        while j >= 0 and key < givenList[j]:
            givenList[j + 1] = givenList[j]
            j -= 1
        givenList[j + 1] = key

insertionSort(givenList)

#prints out to our console the list. 
print("The sorted list is: {} ".format(givenList))
        
        
>>>>>>> ee95c9602ad586e4f878df49fe1fe6e169e9613b
