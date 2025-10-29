def pyth(a,b,c):
    return (a**2) + (b**2) == c**2

def pyth_1000():
    a = 0
    b = 0
    c = 0
    _sum = []
    for a in range(333):
        for b in range(500):
            c = 1000 - a - b
            if pyth(a,b,c):
                _sum =  [a,b,c]
    return _sum

print(pyth_1000())
