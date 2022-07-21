def issubsequence(s1, s2):
 
    n,m = len(s1),len(s2)
    i,j = 0,0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1
     
    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n
 
 
# driver code
s1 = "gksrek"
s2 = "geeksforgeeks"
print(issubsequence(s1, s2))
    
