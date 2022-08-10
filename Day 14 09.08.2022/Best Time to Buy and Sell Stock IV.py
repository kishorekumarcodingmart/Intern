class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        return self.seller(prices,n,k,0)
    
    def seller(self,prices,n,k,ptr):
        if ptr==k:
            return 0
        temp = 0
        ans = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    ans = prices[j] - prices[i] + self.seller(prices[j+1:],len(prices[j+1:]),k,ptr+1)
                temp = max(ans,temp)
        return temp

k = 2

arr = [3,2,6,5,0,3]

node = Solution()

print(node.maxProfit(k,arr))