

import turtle                    # import turtle library
import time
import sys
from collections import deque

win = turtle.Screen()               # define the turtle screen
win.bgcolor("black")                # set the background colour
win.setup(1300,700)                  # setup the dimensions of the working window


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
        self.hideturtle()

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.hideturtle()


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.hideturtle()

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.hideturtle()


grid = [
"+++++++s+++++++++++++++++++++++++++++++++++++++++++",
"+++++++ +++++++++++++++++++++++++++++++++++ +++++++",
"+++++++    +++++++++++++++++++++++++++++    +++++++",
"+++++++      +++++++++++++++++++++++++      +++++++",
"+++++++       +++++++++++++++++++++++       +++++++",
"+++++++                                     +++++++",
"+++++++                                     +++++++",
"+++++++             ++++++++++++            +++++++",
"+++++++               ++++++++              +++++++",
"+++++++                                     +++++++",
"+++++++                                     +++++++",
"+++++++                                     +++++++",
"+++++++         +++++            +++++      +++++++",
"+++++++          +++              +++       +++++++",
"+++++++                  + +                +++++++",
"+++++++                   +                 +++++++",
"+++++++                                     +++++++",
"+++++++                                     +++++++",
"+++++++       ++++++++++++++++++++++++      +++++++",
"+++++++                                     +++++++",
"+++++++                                     +++++++",
"+++++++                                     e++++++",
"+++++++                                     +++++++",
"+++++++                                     +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]


def mazeSetup(grid):                          # define a function called mazeSetup
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -600 + (x * 24)         # move to the x location on the screen 
            screen_y = 300 - (y * 24)          # move to the y location of the screen 

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)
                


def endProgram(win):
    win.exitonclick()
    sys.exit()

def search(x,y):
    dequeF.append((x, y))
    solution[x,y] = x,y

    while len(dequeF) > 0:          # exit while loop when dequeF queue equals zero
        time.sleep(0)
        x, y = dequeF.popleft()     # pop next entry in the dequeF queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell  
            dequeF.append(cell)   # add cell to dequeF list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell dowin
            cell = (x, y - 24)
            solution[cell] = x, y          
            dequeF.append(cell)
            visited.add((x, y - 24))
            

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y          
            dequeF.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            dequeF.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()


def backRoute(x, y):
    red.goto(x, y)
    red.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        red.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        red.stamp()
        x, y = solution[x, y]               # "key value" now becomes the new key

# setup lists
walls = []
path = []
visited = set()
dequeF = deque()
solution = {}                           # solution dictionary


        # class setup
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

mazeSetup(grid)
search(start_x,start_y)
backRoute(end_x, end_y)
endProgram(win)
    
main()
