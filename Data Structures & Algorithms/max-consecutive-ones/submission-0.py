class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = res = 0
        for i in nums:
            if i == 0:
                res = max(res, cnt)
                cnt = 0
            if i == 1:
                cnt += 1
        return max(res, cnt)
