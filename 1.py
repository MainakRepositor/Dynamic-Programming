# 0-1 Knapsack

W,n = map(int,input().split())
wt = list(map(int, input().split()))
val = list(map(int, input().split()))

def knapsack(wt, val, W, n): #base case
    if n==0 or W==0: # the smallest valid input
        return 0
        
    # choice diagram    
    if (wt[n-1]<=W): #when the condition is valid but choice is optional 
        return max(val[n-1] + knapsack(wt,val,W-wt[n-1],n-1), knapsack(wt,val,W,n-1))
        
    elif(wt[n-1]>W): #when the condition is invalid (wt[n-1]>W)
        return knapsack(wt,val,W,n-1)
        
print(knapsack(wt,val,W,n))
