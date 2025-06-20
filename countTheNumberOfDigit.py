# Count the Number of Digits in an Integer 


def count_Digit(n):
    
    count = 0
    num = n
    while num > 0:
        count+=1
        num = num //10

    
    return count
n = 123455
print(count_Digit(n))
