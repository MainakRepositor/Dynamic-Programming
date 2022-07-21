def lcs(str1, str2, m, n):
 
    L = [[0 for i in range(n + 1)]
         for i in range(m + 1)]
 
    # Following steps build L[m+1][n+1]
    # in bottom up fashion. Note that
    # L[i][j] contains length of LCS
    # of str1[0..i-1] and str2[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif(str1[i - 1] == str2[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
 
    # L[m][n] contains length of LCS
    # for X[0..n-1] and Y[0..m-1]
    return L[m][n]
 
# function to find minimum number of deletions and insertions
 
 
def printMinDelAndInsert(str1, str2):
    m = len(str1)
    n = len(str2)
    leng = lcs(str1, str2, m, n)
    print("Minimum number of deletions = ",
          m - leng, sep=' ')
    print("Minimum number of insertions = ",
          n - leng, sep=' ')
 
 
# Driver Code
str1 = "heap"
str2 = "pea"
 
# Function Call
printMinDelAndInsert(str1, str2)
 
