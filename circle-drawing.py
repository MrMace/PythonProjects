from graphics import *
import math


def styleCircle( circle ):
    circle.setFill( 'red' )

def addCircle( centerPoint, color, win ):
    circleObject = Circle( centerPoint, 30 )
    circleObject.setFill( color )
    circleObject.setOutline( color )
    circleObject.draw( win )


def main():
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 200

    win = GraphWin( "Circle Picture", WINDOW_WIDTH, WINDOW_HEIGHT )

    for index in range( 0, 400, 20 ):
        centerPoint = Point( index, math.sin(index / 400 * 2.5 * math.pi) * 50 + WINDOW_HEIGHT / 2 )
        color = color_rgb( int(index / 100 * 255) % 255, 55, 90 )
        addCircle( centerPoint, color, win )

main()