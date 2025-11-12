def missing_numbers(nums: list[int]) -> list[int]:
    ori = set(nums)
    without_missing = set(range(1, nums[-1]+1))
    return list(without_missing - ori)
print(missing_numbers([1, 3, 5, 7]))
print(missing_numbers([1, 4, 5, 7]))

def _____missing_numbers(nums: list[int]) -> list[int]:
    _missing_numbers = []
    for i, num in enumerate(nums):
        while nums[i+1] != num:
            _missing_numbers.append(num+1)
            num += 1
    return _missing_numbers




