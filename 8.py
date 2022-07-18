class Solution:
    def countSubsetSum(self, nums, S):
        n = len(nums)
        dp = [[-1]*(S + 1) for x in range(n + 1)]
        
        for j in range(S + 1):
            dp[0][j] = 0
        
        for i in range(n + 1):
            dp[i][0] = 1
        
        
        for i in range(1, n + 1):
            for j in range(S + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][S]
    
        
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        totalSum = sum(nums)
        
        S = (totalSum + target)//2
        
        if (totalSum + target) % 2 != 0 or totalSum < abs(target):
            return 0
        
        return self.countSubsetSum(nums, S)
