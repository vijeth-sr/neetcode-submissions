class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = {num: i for i, num in enumerate(numbers)}
        for i,n in enumerate(numbers):
            if target - n in numSet:
                    return [min( i+1, numSet[target-n]+1), max( i+1, numSet[target-n]+1)]

                      
                



