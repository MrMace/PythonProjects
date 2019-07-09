import graphics as g

# Get the user's phone battery level
batteryLevel = float( input('What is your phone\'s battery level? '))

# Declare constants for the window
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 100
WINDOW_MARGIN = 20 # space between the edge of the window and andy objects

# Construct the graphics window and set it's fill to black
win = g.GraphWin('Battery Level Indicator', WINDOW_WIDTH, WINDOW_HEIGHT)
win.setBackground('black')

# Construct and draw battery level border
BORDER_WIDTH = 5
batteryMeterBorder = g.Rectangle( g.Point( WINDOW_MARGIN, WINDOW_MARGIN ),
                                  g.Point( WINDOW_WIDTH - WINDOW_MARGIN,
                                           WINDOW_HEIGHT - WINDOW_MARGIN ) )
batteryMeterBorder.setFill('black')
batteryMeterBorder.setOutline( 'white' )
batteryMeterBorder.setWidth( BORDER_WIDTH )
batteryMeterBorder.draw( win )

# Construct the battery meter whose width depends on the battery level: a lower battery level is less wide
BATTERY_METER_MARGIN = 3
TOTAL_METER_MARGIN = WINDOW_MARGIN + BORDER_WIDTH + BATTERY_METER_MARGIN
batteryMeterWidth = batteryLevel * (WINDOW_WIDTH - 2 * TOTAL_METER_MARGIN )
batteryMeter = g.Rectangle( g.Point( TOTAL_METER_MARGIN,
                                     TOTAL_METER_MARGIN ),
                            g.Point( TOTAL_METER_MARGIN + batteryMeterWidth,
                                     WINDOW_HEIGHT - TOTAL_METER_MARGIN))

# If the battery level is 20% or more, fill the meter with white
if batteryLevel >= .2:
    batteryMeter.setFill('white')
# If the battery level is less than 20%, fill the meter with red
if batteryLevel < .2:
    batteryMeter.setFill('red')

# Draw the battery meter in the window
batteryMeter.draw( win )






