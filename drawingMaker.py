import graphics as g

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

win = g.GraphWin('Drawing Generator', WINDOW_WIDTH, WINDOW_HEIGHT)

while True:
    shapeRequest = input("What shape do you want to draw" +
                         "('r' for rectangle, 'c' for circle )? " )
    #condition 1
    while not(shapeRequest == 'c' or shapeRequest == 'r'):
        print("Error: Please enter a valid shape.")
        shapeRequest = input("What shape do you want to draw" +
                         "('r' for rectangle, 'c' for circle )? " )
    
    print()
    shape = None
    
    if shapeRequest == 'c':
        centerX = int(input("Enter the circle's cetner X value: "))
        centerY = int(input("Enter the circle's center Y value: "))
        
        while centerX < 0 or centerX > WINDOW_WIDTH or centerY < 0 or centerY > WINDOW_HEIGHT:
            print("Error: Please enter an X value between" +
                  " 0 and {0} and a Y value between 0 and {1}".format(WINDOW_WIDTH,WINDOW_HEIGHT))
            centerX = int(input("Enter the circle's cetner X value: "))
            centerY = int(input("Enter the circle's center Y value: "))
            
        radius = int(input("Enter the circle's radius: "))
        centerPoint = g.Point(centerX, centerY)
        shape = g.Circle(centerPoint, radius)
            
    else:
        print("skpping rectangles for brevity")
            
        shape.draw(win)
        clickPoint = win.getMouse()
        
    #condition 3
        while clickPoint.y > 50 and clickPoint.y <= 450:
            clickPoint = win.getMouse()
            