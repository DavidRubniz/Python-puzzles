def searchInsert(self, nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        for i, n in enumerate(nums):
            if n > target:
                return max(0, i)
        return len(nums)