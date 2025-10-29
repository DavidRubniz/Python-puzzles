def _smallest_number_division_by_1_20(num=2520):
    while True:
        for i in range(1, 21):
            if num % i != 0:
                break
        else:
            return nun
        num += 1
def smallest_number_division_by_1_20(num=2520):
    while True:
        for i in range(1, 21):
            if num % i != 0:
                break
        else:
            return num
        num += 1

print(smallest_number_division_by_1_20())

