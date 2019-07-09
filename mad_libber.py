#Matt Mace
#BDAT610/week4
#mad-libber


def main():
    
    print("Madlib Maker") #title
    #requested variables
    name = input("Enter your name: ") 
    profession = input("What is your profession: ")
    city = input("Please enter a city: ")
    verb = input("Please enter a verb: ")
    friend = input("Please enter your friends name: ")
    #list of sentences
    sentenceOne = "\nThere once was a {1} named {0}."
    sentenceTwo = "Who lived in {2}. "
    sentenceThree = "{0} liked to {3} and talk with trees."
    sentenceFour = "This bothered {0}'s best friend {4}."
    sentenceFive = "The end."
    #combines all sentences into one list
    combinedSentences = [sentenceOne , sentenceTwo , sentenceThree,sentenceFour,sentenceFive]
    #Goes through each item of the list and displays with the correct var
    for x in combinedSentences:
        print(x.format(name,profession, city,verb,friend))
       
main()