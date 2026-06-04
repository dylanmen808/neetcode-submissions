class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            #if the int is not in our hashmap...
            if not mp[num]:
                #compute the sequence length
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                #compute the left boundary for that num
                mp[num - mp[num - 1]] = mp[num]
                #computre the right boundary for that num
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
                

        
        