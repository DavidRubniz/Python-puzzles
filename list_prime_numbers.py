import math
def the_10001_prime_factor():
    l = []
    n = 3
    while len(l) < 10000:
        for i in range(2, n):
            if n % i == 0:
                n+=1
                break
        else:
            l.append(n)
            n+=1
    return l[-1]
#print(the_10001_prime_factor())
def the_primes_below_two_million():
    l = [2, 3]
    n = 4
    while n < 2000000:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                break
        else:
            l.append(n)
        n += 1
    return sum(l)
print(the_primes_below_two_million())


