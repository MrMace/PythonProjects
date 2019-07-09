#Matt Mace
#BDAT610/week3
#gradient_bar

import graphics as g #import for graphics library
#creates screen
winWidth = 400 #window width
winHeight = 300 #window Height
win = g.GraphWin("Gradient Bar", winWidth,winHeight) 
win.setBackground('red')#verifiy background is not seen under gradient
#vars
numBars = 12 #change this to change outcome
barWidth = winWidth / numBars #sets width of bars
colorChangeAmount = 255 / numBars #sets the number for colorchange
startPointX = 0
startPointY = 0
endPointX = barWidth
endPointY = winHeight #bottom of screen
colorChanger = 0



#loops through and creates rectangles Fills them with color 
for index in range(numBars):
    #creates the rectangle
    gradientLine = g.Rectangle(g.Point(startPointX,startPointY),g.Point(endPointX,endPointY))
    gradientLine.setFill(g.color_rgb(0,int(colorChanger),0)) #fills the rectangle
    gradientLine.setWidth(0)
    gradientLine.draw(win)#draws the Rectangle to screen
    startPointX = endPointX #sets starting position of next Rectangle
    endPointX = endPointX + barWidth #sets ending position next Rectangle
    colorChanger = colorChanger + colorChangeAmount #changes the color 
    
    

