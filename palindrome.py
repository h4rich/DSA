# Palindrome Number or Not 


def palindrome_num(n):
    num = n 
    result = 0

    while num > 0:
        ld = num % 10 
        result = (result * 10) +ld
        num = num //10 


    return n == result

n = 121

print(palindrome_num(n))



