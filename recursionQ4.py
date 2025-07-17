# Find the Fibonacci Number Using recursion 
def fibonacci(num):
    if num ==0 or num == 1:
        return num
    
    return fibonacci(num-1)+fibonacci(num-2)

fib = fibonacci(9)
print(fib)

