from datetime import datetime
startTime = datetime.now()

fibonacci_storage = {}

def fibonacci(n):
    #If we have stored the value, then return it.
    if n in fibonacci_storage:
        return fibonacci_storage[n]
    
    #computes the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n -2)
        
    #store the value and return
    fibonacci_storage[n] = value
    return value

for n in range(1, 10 + 1):
    print(n, ":",  fibonacci(n))

print(datetime.now() - startTime)
