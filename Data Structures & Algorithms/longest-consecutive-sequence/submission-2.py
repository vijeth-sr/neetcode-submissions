class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        max=0
        for num in nums:
            c=1
            n=num
            while n+1 in nums:
                c+=1
                n+=1
                
            if c>max:
                max=c
        return max
            
                

            
            

