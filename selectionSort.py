#ListGiven 
givenList =  [1,2,5,4,3,6,7,8,9,10]

'''
This is the Selection sorting algorithm that sorts the list by going through it and finding the smallest
element from a unsorted part and puts it at the beginning.
In every iteration of the selection sort, the minimum element from the usorted list is picked and moved
to the sorted list. 
'''

def selectionSort(givenList):
    
    listLen = len(givenList) #gets length of the list
    
    #goes through the length of the list
    for i in range(listLen):
        
        #Finds the smallest element remaining in
        #the list 
        minIndex = i
        
        for j in range( i + 1, listLen):
            
            if givenList[minIndex] < givenList[j]:
                minIndex = j
         
         #swaps out the smallest element with the first element. 
        givenList[i], givenList[minIndex] = givenList[minIndex], givenList[i]
        
selectionSort(givenList) #calls the function

#prints out to our console the list. 
print("The sorted list is: {} ".format(givenList))