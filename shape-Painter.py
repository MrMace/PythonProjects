from graphics import *


def getColor ( colorString ):
    tokens = colorString.split(',')
    if len( tokens ) == 3:
        return color_rgb( int(tokens[0] ), int( tokens[1] ), int( tokens[2] ))
    elif len( colorString) > 0:
        return colorString
    else:
        return 'white'