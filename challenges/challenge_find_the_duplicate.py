def find_duplicate(nums):
    if not isinstance(nums, list) or not all(isinstance(n, int) for n in nums):
        return False

    if any(n < 1 for n in nums):
        return False

    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False
