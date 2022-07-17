def findSubsetSum (A,  N, summ):
    
   # First, we initialize the matrix
   
   matrix = [[1 for x in range(summ+1)] for x in range(N+1)]
   for k in range(1,summ+1):
       matrix[0][k] = 0
   for k in range(1,N+1):
       matrix[k][0] = 1
   
   for k in range(1,N+1):
       for l in range(1,summ+1):
           # If element value is greater than the sum value
           if(A[k - 1] > l):
               matrix[k][l] = matrix[k - 1][l]
           else:
               matrix[k][l] = matrix[k - 1][l] + matrix[k - 1][l - A[k - 1]];
           
   
   return matrix[N][summ]
A = [2,3,5,6,8,10]
N = len(A)
summ = 10 
print(findSubsetSum(A, N, summ))
