numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def reverse(numList):
     #base case return  if we reach end. 
    if len(numList) == 0:
        return numList      
    else:
        #Indexing selecting the front one and concat with end of list.
        return reverse(numList[1:]) + numList[:1]
    
print("Number List Regular: {}".format(numList))
print("The List Reversed: {}".format(reverse(numList)))