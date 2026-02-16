def is_prime(n):
    import math

    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        x = int(math.sqrt(n)) + 1
        for i in range(3, x):
            if n % i == 0:
                return False
        return True


def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        x = abs(a * b) // gcd(a , b)
        return x 
    
def generate_password(length):
    import random
    
    result= []
    
    pool = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for _ in range(length):
        x = random.randint(0,len(pool) -1)
        result.append(pool[x])
        
    return  "".join(result)
        
    
     
