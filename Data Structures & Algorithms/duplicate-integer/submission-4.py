class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                
                if nums[i] == nums[j]:
                    return True
        return False

        seen = set()
        for num in nums:
            if (num in seen):
                return True
            if num == ".":
                continue
            seen.add(num)
        return False
        return len(set(nums))<len(nums)
            
        


