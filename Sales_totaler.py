inputFileName = input("Enter sales file name: ")
outputFileName = input("Enter name for total sales file: ")

inFile = open(inputFileName, 'r')

amountSeq = inFile.readlines()

for amount in amountSeq:
    splitAmount = amount.split(" ")
    amountOne = splitAmount[0]
    amountTwo = splitAmount[1]
    amountOne = float(amountOne[1:8])
    amountTwo = float(amountTwo[1:8])      
    lineTotal = amountOne + amountTwo
    
    
    #print(amountOne , amountTwo, lineTotal)
    print("${0:>8} ${1:>8} ${2:>8}".format(amountOne, amountTwo, lineTotal))

