class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l=0
        res =0
        for r in range(len(s)):
            count[s[r]] = 1+ count[s[r]]

            if (r+1-l) - max(count.values()) <=k:

                res = max(res, r-l+1)
                continue
            else:
                count[s[l]]-=1
                l+=1

        
        return res




           




        return total

            
            
            

        








        