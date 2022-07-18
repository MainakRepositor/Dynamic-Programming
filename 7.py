def subsetSum(arr,n,s):
    n = len(arr)
    dp = [[-1]*(s+1) for x in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = 0
    for j in range(s+1):
        dp[0][j] = 1 
        
    for i in range(1,n+1):
        for j in range(s+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][s]
    
    def countSumsetSum(arr, n, diff):
        s = 0
        for i in range(n):
            s += arr[i]
            
        reqSum = (diff+s)//2
        return subsetSum(arr,n,reqSum)
        
arr = [1,7,4,8]
diff = 3
n = len(arr)
print(subsetSum(arr,n,diff))
        
    
    
        
    
    
