MAX = 1000
 
# Return the maximum size of
# substring of X which is
# substring in Y.
def maxSubsequenceSubstring(x, y, n, m):
    dp = [[0 for i in range(MAX)]
             for i in range(MAX)]
              
    # Initialize the dp[][] to 0.
 
    # Calculating value for each element.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
             
            # If alphabet of string
            # X and Y are equal make
            # dp[i][j] = 1 + dp[i-1][j-1]
            if(x[j - 1] == y[i - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
 
            # Else copy the previous value
            # in the row i.e dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j - 1]
                 
    # Finding the maximum length
    ans = 0
    for i in range(1, m + 1):
        ans = max(ans, dp[i][n])
    return ans
 
# Driver Code
x = "ABCD"
y = "BACDBDCD"
n = len(x)
m = len(y)
print(maxSubsequenceSubstring(x, y, n, m))
