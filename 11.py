# Dynamic Programming Python implementation of Coin Change Problem - II

def change(amount,coins):
        dp = [0]*(amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount + 1):
                if coin + i < amount + 1:
                    dp[coin + i] += dp[i]
        return dp[amount]

# Driver program to test above function
arr = [1, 2, 5]

n = 5
print(change(n,arr))

