dp = [[-1 for i in range(1001)] 
          for j in range(1001)]
  
def isPal(s, i, j):
      
    # Base condition
    if (i > j):
        return 1
  
    # Check if the recursive tree
    # for given i, j
    # has already been executed
    if (dp[i][j] != -1):
        return dp[i][j]
  
    # If first and last characters of 
    # substring are unequal
    if (s[i] != s[j]):
        dp[i][j] = 0
        return dp[i][j]
          
    # Memoization
    dp[i][j] = isPal(s, i + 1, j - 1)
      
    return dp[i][j]
  
def countSubstrings(s):
      
    n = len(s)
  
    count = 0
  
    # 2 for loops are required to check for
    # all the palindromes in the string.
    for i in range(n):
        for j in range(i + 1, n):
              
            # Increment count for every palindrome
            if (isPal(s, i, j)):
                count += 1
  
    # Return total palindromic substrings
    return count
  
# Driver code
s = "abbaeae"
  
print(countSubstrings(s))
  
