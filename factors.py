# Print the factors or divisors of a given Number 

def printFactors(n):
    num = n
    result = []
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)

    return result    

n = 15
print(printFactors(n))