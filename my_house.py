#Matt Mace
#BDAT610/week3
#my_house
#Rectange = 8, Lines = 2, Circles = 1, text labels = 3, colors=18

import random as r
import graphics as g

#draw the screen 
win = g.GraphWin("My House", 400,300)
screenCenter = g.Point(200,150)#center of screen



def main():
    #The Skybox
    skyBox = g.Rectangle(g.Point(0,0),g.Point(400,300))
    skyBox.setFill("lightblue")
    skyBox.setWidth(0)
    skyBox.draw(win)
    #The Sun
    sun = g.Circle(screenCenter, 50)
    sun.setFill("yellow")
    sun.setWidth(0)
    
    #The Ground
    ground = skyBox.clone()
    ground.move(0,150)
    ground.setFill("forestgreen")
    ground.setWidth(0)
    #The Road
    road = g.Polygon(screenCenter,g.Point(0,300),g.Point(400,300),screenCenter)
    road.setFill('grey')
    road.setWidth(0)
    road.setOutline('')
    
    #The House
    house = g.Polygon(g.Point(0,228),g.Point(96,228),g.Point(140,195),g.Point(140,45),g.Point(0,45))
    #house Roof
    houseRoof = g.Polygon(g.Point(140,45),g.Point(95,-5),g.Point(96,46),g.Point(140,46))
    houseRoof.setFill("brown")
    houseRoof.setOutline('')
    houseRoof.setWidth(0)
    #House Roof Second Part
    houseRoofDs = g.Rectangle(g.Point(96,0),g.Point(0,46))
    houseRoofDs.setFill('darkred')
    houseRoofDs.setWidth(0)
    #Gives house Colors
    house2 = g.Rectangle(g.Point(0,45),g.Point(96,228))
    house.setWidth(0)
    house2.setWidth(0)
    house.setFill('darkorange')
    house2.setFill('chocolate')
    
    #door of house
    door = g.Rectangle(g.Point(30,229),g.Point(70,175))
    door.setFill('saddlebrown')
    door.setWidth(0)
    #door handle
    doorHandle = g.Point(64,204)
    doorHandle.setFill("gold")
    #door step
    doorStep = g.Rectangle(g.Point(30,229),g.Point(70,240))
    doorStep.setFill('dimgrey')
    doorStep.setWidth(0)
    
    #window o1 front side of house
    windowFrontsideOne = g.Rectangle(g.Point(7,125),g.Point(43,75))
    windowFrontsideOne.setFill('linen')
    windowFrontsideOne.setOutline('saddlebrown')
    #window 2 on front of house
    windowFrontsideTwo = windowFrontsideOne.clone()
    windowFrontsideTwo.move(43,0)
    #window 1 on side of house
    windowOneSide = g.Rectangle(g.Point(105,76), g.Point(125,121))
    windowOneSide.setFill('linen')
    windowOneSide.setOutline('saddlebrown')
    #window 2 on side of house
    windowTwoSide= windowOneSide.clone()
    windowTwoSide.move(0, 75)
    #signPost
    signPost = g.Line(g.Point(335,220),g.Point(335,180))
    signPost.setWidth(5)
    signPost.setFill('white')
    
    #Actual Sign
    sign = g.Rectangle(g.Point(290,175),g.Point(335,210))
    sign.setFill('white')
    sign.setWidth(0)
    #Sign Text label
    signLandText = g.Text(g.Point(315,185),"Land")
    signSaleText = g.Text(g.Point(315,200),"Sale")
   
   #horizon Line
    horizon = g.Line(g.Point(0,150),g.Point(400,150))
    horizon.setOutline('darkgreen')


    #draws everything
    sun.draw(win)
    ground.draw(win)
    road.draw(win)
    horizon.draw(win)
    house.draw(win)
    house2.draw(win)
    houseRoof.draw(win)
    houseRoofDs.draw(win)
    door.draw(win)
    doorStep.draw(win)
    doorHandle.draw(win)
    windowFrontsideOne.draw(win)
    windowFrontsideTwo.draw(win)
    windowOneSide.draw(win)
    windowTwoSide.draw(win)
    signPost.draw(win)
    sign.draw(win)
    signLandText.draw(win)
    signSaleText.draw(win)
   
    
    #waits for mouse click
    win.getMouse()
    
    #changes scene
    sun.move(125,-80)
    sun.setFill('white')
    skyBox.setFill('black')
    ground.setFill('olive')
    house.setFill('darksalmon')
    house2.setFill('sienna')
    windowFrontsideOne.setFill('yellow')
    windowFrontsideTwo.setFill('dimgray')
    windowOneSide.setFill('dimGray')
    windowTwoSide.setFill('yellow')

    #creates random Stars
    for index in range(5):
        starx = r.randint(150,400)
        stary = r.randint(5,135)
        star = g.Point(starx, stary)
        star.setFill('white')
        star.draw(win)
        
        


main()

#lets users keep interacting 5x
for index in range(5):
    win.getMouse()
    main()
    
#window close warning
closeWarning = g.Text(g.Point(200,150),"One More Click This Window Will Close!")
closeWarning.setFill('red')
closeWarning.draw(win)
#on mouse click closes window
win.getMouse()
win.close()


