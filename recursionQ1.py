# Find the factorial of the Number 

def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num-1)

fact = factorial(5)
print(fact)

