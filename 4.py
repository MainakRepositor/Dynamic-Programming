def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return false
 
    k = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        k[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        k[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            k[i][j] = k[i][j - 1]
 
            if i >= arr[j - 1]:
                k[i][j] = (k[i][j] or
                              k[i - arr[j - 1]][j - 1])
 
    return k[sum // 2][n]
 
 
# Driver Code
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
 
# Function call
print(findPartition(arr, n))
