#Matt Mace
#BDAT610/week7
#randomShapes

import random

"""
Creates a text file that generates a user amount of shapes to use with the shape_painter.py program.
"""
    
def getShape(): #gets a random shape either Rectangle or Circle
    shapes = ["Rectangle", "Circle"]    
    return random.choice(shapes)

def randomXY(): #Gets random X Y coord when called
    return random.randrange(1,500)

def randomColorBlue(): #Gets a random blue color for RGB
    return random.randrange(192,255)

def getColorRed(): #Gets the Red Color when called
    return 32

def getColorGreen(): #Gets the Green Color when called
    return 208

def getRGBColors(): #Get all the colors for RGB colors combines and returns
    r = getColorRed()
    g = getColorGreen()
    b = randomColorBlue()
    rgb = r,g,b
    return rgb

def getStartCoord(): #Creates starting coords.
    stXPt = randomXY()
    stYPt = randomXY()
    return stXPt, stYPt

def getEndCoord(stXPt, stYPt): #Creates and returns end coordniates based on start point values and randomizes.
    endXPt = random.randrange(stXPt, 500) 
    endYPt = random.randrange(stYPt, 500)
    return endXPt, endYPt

def getRectangleShape(startingCoord, endingCoord): #sets up the rectangle starting points and endpoints.
    startingCoord = coordniateStripperP(getStartCoord()) #Gets start coords, and strips ()
    stXPt,stYPt = map(int,startingCoord.split(','))   #Makes the start x,y into int, and removes ,.
    endingCoord = coordniateStripperP(getEndCoord(stXPt,stYPt)) #removes () and gets ending coords.
    #endXPt,endYPt = map(int,endingCoord.split(','))
    return startingCoord,endingCoord

def coordniateStripperP(x): #converts string removes ()
    return str(x).strip('()')

def getCircleRadius(): #Gets random radius for circle
    return random.randrange(5,50)

def main():
    outputFileName = input("Enter the drawing file name to create: ") #Gets file name.
    outFile = open(outputFileName, "w") #opens file to write to it.
    numOfShapes = int(input("Enter the number of shapes to make: ")) #allows uers to input number of random shapes.
    for i in range(numOfShapes):  #Loops through number of shapes and post to document.
        startingCoord = None 
        endingCoord = None
        circleRadius = None
        rgb = coordniateStripperP(getRGBColors()) #Gets RGB from function and sends to stripper to remove()
        shape = getShape() #Gets the shape
        if shape == 'Rectangle': #If it is rectngle gets coordniates and post them into the file.
            startingCoord, endingCoord = getRectangleShape(startingCoord, endingCoord)
            print('{}; {}; {}; {}'.format(shape, startingCoord,endingCoord,rgb),file=outFile)
                    
        else:#If it is circle gets coordniates, and radius and post them into the file.
            startingCoord = getStartCoord()
            startingCoord = coordniateStripperP(startingCoord)
            circleRadius = getCircleRadius()
            print('{}; {}; {}; {}'.format(shape, startingCoord,circleRadius,rgb),file=outFile)
        
    outFile.close() #closes the file.

main()
        

    
    
    
    
 
    
