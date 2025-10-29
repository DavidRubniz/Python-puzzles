def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

# Example usage:
#print(largest_prime_factor(600851475143))



def is_secure(password:str='Qwefgfgf', length:int=0, digit:bool=False, uppercase:bool=False, lowercase:bool=False)->tuple:
    if not password:
        return length, digit, uppercase, lowercase
    if str(password)[-1].isupper():
        uppercase = True
    elif str(password)[-1].islower():
        lowercase = True
    elif str(password)[-1].isdigit():
        digit = True
    length += 1
    new_st = password[:-1]
    if not uppercase or not lowercase or not digit or length < 8:
        return is_secure(new_st, length, digit, uppercase, lowercase)
    return(length, digit, uppercase, lowercase)
length, digit, uppercase, lowercase = is_secure()
print(is_secure())
if length >= 8 and digit and uppercase and lowercase:
    print('good password')
else:
    print('bad password')

