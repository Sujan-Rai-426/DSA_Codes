
# LEETCODE Question no:-[ 121. Best Time to Buy and Sell Stock ]

# Function code to find the best time to buy and sell stocks to get maximum profit
# Using sliding window
# TIME COMPLEXITY -> O(n)
# SPACE COMPLECITY -> O(1)  

# l, r index represent possible buy day and sell day to earn max profit respectively

def Stock_Assistant(Prices):
    
    max_profit = int()
    l, r = 0, 1
    for r in range(len(Prices)):
        
        if Prices[r] < Prices[l]:
            l = r
        profit = Prices[r] - Prices[l]
        max_profit = max(profit, max_profit)
    return max_profit

integer_list = list(map(int, input("Enter a comma-separated string of numbers: ").split(',')))
print("Maxmimu Profit earned:", Stock_Assistant(integer_list))
