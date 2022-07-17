def minDifference(arr, n):
    sum = 0;
    for i in range(n):
        sum += arr[i];
    y = sum // 2 + 1;
     
    # dp[i] gives whether is it possible to get i as
    # sum of elements dd is helper variable we use dd
    # to ignoring duplicates
    dp = [False for i in range(y)]
    dd = [False for i in range(y)]
     
    # Initialising dp and dd
     
    # sum = 0 is possible
    dd[0] = True;
    for i in range(n):
       
        # updating dd[k] as True if k can be formed
        # using elements from 1 to i+1
        for j in range(y):
            if (j + arr[i] < y and dp[j]):
                dd[j + arr[i]] = True;
         
        # updating dd
        for j in range(y):
            if (dd[j]):
                dp[j] = True;
            dd[j] = False; # reset dd
         
    # checking the number from sum/2 to 1 which is
    # possible to get as sum
    for i in range(y-1, 0, -1):
        if (dp[i]):
            return (sum - 2 * i);
           
        # since i is possible to form then another
        # number is sum-i so mindifference is sum-i-i
    return 0;
 
 
if __name__ == '__main__':
 
    arr = [ 1, 6, 11, 5 ];
    n = len(arr);
    print(minDifference(arr, n));
 
