# Reverse the Number 


def reverse_Number(n):
    num = n

    while num > 0:
        last_digit= num %10
        print(last_digit)
        num = num //10 



n = 1234
print(reverse_Number(n))  
