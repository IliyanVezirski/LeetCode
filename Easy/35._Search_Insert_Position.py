class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target < nums[0]:
            return 0
        elif target in nums:
            return nums.index(target)
        else:
            for num in range(len(nums)-1,-1,-1):
                if nums[num] < target:
                    index_target = num + 1
                    return index_target