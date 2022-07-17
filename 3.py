def isSubsetSum(arr, n, sum): 
      
    # The value of subset[i][j] will be  
    # true if there is a 
    # subset of set[0..j-1] with sum equal to i 
    subset =([[False for i in range(sum + 1)]  
            for i in range(n + 1)]) 
      
    # If sum is 0, then answer is true  
    for i in range(n + 1): 
        subset[i][0] = True
          
    # If sum is not 0 and set is empty,  
    # then answer is false  
    for i in range(1, sum + 1): 
         subset[0][i]= False
              
    # Fill the subset table in bottom up manner 
    for i in range(1, n + 1): 
        for j in range(1, sum + 1): 
            if j<arr[i-1]: 
                subset[i][j] = subset[i-1][j] 
            if j>= arr[i-1]: 
                subset[i][j] = (subset[i-1][j] or 
                                subset[i - 1][j-arr[i-1]]) 
      
    # uncomment this code to print table  
    # for i in range(n + 1): 
    # for j in range(sum + 1): 
    # print (subset[i][j], end =" ") 
    # print() 
    return subset[n][sum] 
          
# Driver code 
if __name__=='__main__': 
    arr = [2, 3, 7, 8, 10] 
    sum = 11
    n = len(arr) 
    print(isSubsetSum(arr, n, sum))
        
