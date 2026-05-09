class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        print(nums)
        max=0
        for num in numSet:
            c=1
            
            while num+1 in numSet:
                c+=1
                num+=1
                
            if c>max:
                max=c
        return max
                

            
            

