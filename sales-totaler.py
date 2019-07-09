#Matt Mace
#BDAT610/week4
#sales-totaler

def main():
    inputFileName = input("Enter sales file name: ")#file name to open
    outputFileName = input("Enter name for total sales file: ")#file name to create

    inFile = open(inputFileName, 'r')#opens and reads file
    outFile = open(outputFileName, 'w')#opens the out file

    amountSeq = inFile.readlines()#read the lines
#runs through the file and seperates at the spaces each line then
#turns the string into a float. 
    for amount in amountSeq:
        #another way to do.
        #splitAmount = amount.split(" ")
        #amountOne = splitAmount[0]
        #amountTwo = splitAmount[1]
        ##########
        amountOne, amountTwo = amount.split(' ') 
        amountOne = float(amountOne[1:8])
        amountTwo = float(amountTwo[1:8])
        lineTotal = amountOne + amountTwo#add lines together get total amount.
        #formats the output into right align postion
        finalOutput = "${0:>8} ${1:>8} ${2:>8}".format(amountOne, amountTwo, lineTotal)
        #prints to output file name. 
        print(finalOutput, file=outFile)
    
    inFile.close()#close input file
    outFile.close()#close output file.
    print("\nDone writing totals to {0}".format(outputFileName))

main()
    
    

