a = input("Enter the first string: ")
b = input("Enter the second string: ")


if len(a) > len(b):
    print("The longer string is {0}".format(a))
    
elif len(b) > len(a):
  #  if len(b) > len(a):
        print("The longer string is {0}".format(b))
else:
    print("It's a tie")