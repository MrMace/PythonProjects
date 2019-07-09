

try:
    p1_x = int(input("Enter p1_x value: "))
    p1_y = int(input("Enter p1_y value: "))

    print("")

    p2_x = int(input("Enter p2_x value: "))
    p2_y = int(input("Enter p2_y value: "))

    slope = (p2_y - p1_y)/ (p2_x - p1_x)

    print("The slope is {0:0.3f}.".format(slope))
    
except ZeroDivisionError:
    print("You entered in two x values that were the same")
    
except ValueError:
    print("You entered non integer characters")
    