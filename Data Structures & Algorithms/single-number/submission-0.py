class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            duplicate=False
            for j in range(len(nums)):
                if i!=j and nums[i]==nums[j]:
                    duplicate=True
            if duplicate==False:
                return nums[i]

        