a = 5
b = 5
c = 25
maxVal = -1

numOfValues = int(input("Enter the number of values: "))

maxVal = int(input("Enter the first Value: "))
for index in range(numOfvalues - 1):
    nextVal = int(input("Enter the first Value: "))
    if nextVal > maxVal:
        maxVal = nextVal
#maxVal = a
#if b > maxVal:
   # maxVal = b
#if c > maxVal:
   # maxVal = c


#if a >= b and a>= c:
   # maxVal = a
#elif b >= a and b >= c:
   # maxVal = b
#elif c >=a and c >=b:
   # maxVal = c
#else:
   # print(maxVal)
   
#if a >= b:
   # if a >=c:
      #  maxVal = a
    #else:
   #     maxVal = c
#else: #b > a
 #   if b >=c:
     #   maxVal = b
  #else:
       # maxVal = c
#print(maxVal)