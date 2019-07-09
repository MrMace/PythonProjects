from math import sin, cos, radians



def main():
    angle = float(input("Enter the launch angle (in degrees): "))
    vel = float(input("Enter the initial velocity (in meters/sec): "))
    h0 = float(input("Enter the initial height (in meters): "))
    time = float(input("Enter the time interval between position calculations: "))
    
    #convert angles to radians
    theta = math.radians(angle)
    
    #set the initial position and velocities in x and y directions
    xpos = 0
    xvel = velocity * math.cos(theta)
    ypos = 0
    yvel = velocity * math.sin(theta)
    
    #loops until ball hits the ground
    while ypos >= 0.0:
        #calculate position and velocity in time seconds
        xpos = xpos + time * xvel
        yvel1 = yvel - time * 9.8
        ypos = yps + time * (yvel + yvel1)/2.0
        yvel = yvel1
        
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))
    
main()