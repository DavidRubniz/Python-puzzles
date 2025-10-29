def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return i, d[m]
        d[n] = i