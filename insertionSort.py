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
        
        