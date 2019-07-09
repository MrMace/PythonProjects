
countOfEs = 0
totalLengthOfInputs = 0
numOfWords = 0

shouldContinue = 'y'

#for index in range(numOfWords):
while shouldContinue == 'y':
    numOfWords = numOfWords + 1
    inputWord = input("Enter word {0}: ".format(numOfWords))
    countOfEs = countOfEs + inputWord.count('e')
    totalLengthOfInputs = totalLengthOfInputs + len(inputWord)
    
    shouldContinue = input("Do you want to continue (y/n)? ")
    
print("Total e\'s seen: ",countOfEs)
print("Pct of e\'s: {:0.2}%".format(countOfEs/ totalLengthOfInputs))
print("Average e\'s seen: {:0.2}".format(countOfEs / numOfWords))
      