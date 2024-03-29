from datetime import datetime
startTime = datetime.now()

# Python program to display the Fibonacci sequence up to n-th term using recursive functions
def recur_fibo(n):
    
    if n<= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
#chage value for a different result
nterms= 11

#uncomment to take input from the user.
#nterms = int(input("How many terms? "))

#check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer ")
else:
    print("Fibonacci sequence: ")
    for i in range(nterms):
        print(recur_fibo(i))
        
print(datetime.now() - startTime)
        

    
    