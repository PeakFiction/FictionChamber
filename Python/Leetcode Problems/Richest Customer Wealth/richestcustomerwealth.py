class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        
        for customer_accounts in accounts:
            current_wealth = 0

            for amount in customer_accounts:
                current_wealth = current_wealth + amount
            
            if current_wealth > max_wealth:
                max_wealth = current_wealth
                
        return max_wealth
    
rows = int

