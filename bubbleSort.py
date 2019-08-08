#List
givenList =  [1,2,3,6,5,4,7,8,9,10]

'''
This is the bubble sort algorithm that keeps exchangeing the adjacent elements if
they are in the wrong order. This is the simplist sorting algorithm.
'''
def bubbleSort(givenList): #bubbleSort Function
    
    listLen = len(givenList) #gets length of the list
    
    for i in range(listLen): #Goes through all the list elements
        
        #Goes through the list, swaps the element if the next one
        #is greater then moves to the next element.
        for j in range(0, listLen - i - 1):
            
            if givenList[j] < givenList[j + 1]:
                givenList[j], givenList[j + 1] = givenList[j + 1], givenList[j]
                
bubbleSort(givenList) #calls our bubble sort function/ passes list

#prints out to our console the list. 
print("The sorted list is: {} ".format(givenList))