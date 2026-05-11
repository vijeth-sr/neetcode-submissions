class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l,r = 0, len(prices)-1
        # res=0

        # while l<r:
        #     res = max (res, prices[r]-prices[l])

        #     if prices[l]>prices[r]:
        #         l+=1
        #     else:
        #         r-=1
        
        # return res

        res=0

        for i in range(0,len(prices)):
            for j in range(i+1, len(prices)):
                res = max(res, prices[j]-prices[i])

        return res

        