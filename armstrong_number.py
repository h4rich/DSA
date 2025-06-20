# Armstrong Number or not 


def armstrong_Number(n):
    num = n
    total = 0
    nod = len(str(n))    # nod = number of digit 

    while num > 0: 
        ld = num % 10              # ld = last digit 
        total = total + (ld**nod)
        num = num//10 


    return n == total 

n= 153
print(armstrong_Number(n))
    