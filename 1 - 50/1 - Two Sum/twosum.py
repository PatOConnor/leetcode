class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in nums:
                #check for doubles
                if nums.index(tmp) == i:
                    continue
                return [i, nums.index(tmp)]