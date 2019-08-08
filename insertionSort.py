#ListGiven
givenList =  [1,2,3,5,4,6,7,8,9,10]

'''
This is the Insertion sorting algorithm. Starts from 1 index in the list not 0 We compare our key var with the
elements before it if key is less than first element we instert the key element before first. If key is greater than first we inster after first element.
We make a third element and compare the element to the left and insert it in the right position. Reapeat until ordered.
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