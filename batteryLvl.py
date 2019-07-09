batteryLevel = float(input("Enter the phone\'s battery level: "))

if batteryLevel >= .2:
    print("Fill the battery with WHITE")

if batteryLevel < .2:
    print("Fill the battery with RED")
    