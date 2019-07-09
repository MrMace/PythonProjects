
kmVal = float(input("Enter the distance in Kilometers: "))

if kmVal >= 0:
    milesVal = kmVal / 1.609
    print("{0:0.2f} km is the same as {1:0.2f} mi.".format(kmVal, milesVal))

else:
    print("You cannot enter a negative Km Value")
    
print("Thanks for converting")