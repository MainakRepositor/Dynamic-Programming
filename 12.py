def maxProd(n):
    val= [0 for i in range(n+1)];
   
   # Build the table val in bottom up manner and return
   # the last entry from the table
    for i in range(1,n+1):
        max_val = 0;
        for j in range(1,i):
            max_val = max(max_val, (i-j)*j, j*val[i-j])
        val[i] = max_val;
    return val[n]
 
  
# Driver program to test above functions
print("Maximum Product is ", maxProd(10))
