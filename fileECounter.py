fileNames = ["words_1.csv","words_2.csv","words_3.csv"]
totalNumOfEs = 0

for fileName in fileNames:
    wordsFile = open(fileName, 'r')
    
    nextLine = wordsFile.readline()
    while nextLine != '':
        words = nextLine.split(',')
        for word in words:
            numOfEs = word.count('e')
            totalNumOfEs = totalNumOfEs + numOfEs
        nextLine = wordsFile.readline()
    wordsFile.close()    
print("The total number of e\'s is {0}. ".format(totalNumOfEs))
    
