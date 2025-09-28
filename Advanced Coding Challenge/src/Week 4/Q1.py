# 1. Digital Currency
# Problem Description

# You are engaged in buying and selling one digital currency called AndyCoin. And the price of each coin changes each day. On each day, you can decide to buy or sell the coin you bought (You can buy the coin and sell it on the same day). However, you are allowed to hold one coin at most. 

# You will be given an array that contains the prices of the coin each day. Take the array [1, 2, 3] as an example, the first element in the array is the price on the first day, the second element is the price on the second day, and so on.

# Print out the maximum profit based on the given prices.

# Sample Input/Output

# Case 1

# Input

# 1 2 3
# Output

# 2
# Case 2

# Input

# 2 3 5 1 8 9 2
# Output

# 11
# Case 3

# Input

# 9 1 2 4 8 2
# Output

# 7
def cal_price(prices):
    total = 0
    for i in range(1,len(prices)):
        if prices[i - 1] <= prices[i]:
            total += prices[i] - prices[i - 1]
    return total
        
def main():

    prices = input().split()
    prices = list(map(int, prices))
    print(cal_price(prices))

main()