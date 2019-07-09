from graphics import *


class DieView:
    """ Die View is a widget that displays a graphical represenation
of a standard six-sided die. """
    
    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
        d1= DieView(myWin, Point(40,50),20)
        creates a die centered at (40, 50) having sides
        of length 20. """
        
    
        #First define some standard values
        self.win = win  #save this for drawing pops later
        self.background = 'white' #color of die face
        self.foreground = 'black' #color of the pops
        self.psize = 0.1 * size #radius of each pop
        hsize = size / 2.0 #half the size of the die
        offset = 0.6 * hsize #distance from cetner to outer pops
        
        #create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)
        
        #Create 7 circles for standard pip locations
        self.pip1 = self.__makePip(cx-offset, cy-offset)
        self.pip2 = self.__makePip(cx-offset, cy)
        self.pip3 = self.__makePip(cx-offset, cy+offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx+offset, cy-offset)
        self.pip6 = self.__makePip(cx+offset, cy)
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        
        #Draw an inital value
        self.setValue(1)
        
    def __makePip(self, x, y):
        "Internal helper method to draw a pop at (x,y)"
        pip = Circle(Point(x,y),self.psize)
        
        