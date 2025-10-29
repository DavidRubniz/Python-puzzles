def the_largest_palindromic_in_3_numbers():
    largest = 0
    for i in range(1000):
        for j in range(1000):
            p = str(i*j)
            if p == p[::-1]:
                if int(p) > largest:
                    largest=int(p)
    return largest
print(the_largest_palindromic_in_3_numbers())


