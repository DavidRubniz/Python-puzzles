def palindrome(num):
    snum = str(num)
    snum1 = snum[::-1]
    print(snum)
    if snum == snum1:
        return True
    return False

d = palindrome(-121)
print(d)