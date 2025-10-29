def the_difference_between_squer_of_to_sum_of_squer():
    l = sum(range(101))**2
    l2 = sum(i**2 for i in range(101))
    return l - l2
print(the_difference_between_squer_of_to_sum_of_squer())


