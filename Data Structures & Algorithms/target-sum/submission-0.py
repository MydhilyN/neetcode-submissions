from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=[defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0]=1
        for i in range(len(nums)):
            for cumsum,count in dp[i].items():
                dp[i+1][cumsum+nums[i]]+=count
                dp[i+1][cumsum-nums[i]]+=count
        return dp[len(nums)][target]