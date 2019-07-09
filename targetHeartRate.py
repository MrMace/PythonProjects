def getAge():
    return int(input("Enter your age in years: "))

def getMaxHeartRate(age):
    return 206.9 - (0.67 * age)

def getTargetHeartRate(maxHeartRate):
    return 0.65 * maxHeartRate

def main():
    age = getAge()
    maxHeartRate = getMaxHeartRate(age)
    targetRate = int(getTargetHeartRate(maxHeartRate))
    print("Your target fat-burning heart rate is: {} bpm.".format(targetRate))
    
main()