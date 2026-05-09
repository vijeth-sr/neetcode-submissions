class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res,p, zero_cnt= [],1,0
        for n in nums:
            if 0!=n:
                p=p*n
            else:
                zero_cnt+=1
        if zero_cnt > 1 : return[0]*len(nums)
                

        
        for n in nums:
            if zero_cnt:
                if n==0 :
                    res.append(p)
                else: res.append(0)
            else:
                res.append(int(p//n))
        return res
            

        

        
        
        


        